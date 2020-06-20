import json
import sys


class Bond:
    """
    Default contructor takes input as a jsonstring and provides method to extract fields from the Bond
    """

    def __init__(self, data):
        self.data = data

    def get_amount_outstanding(self):
        return int(self.data['amount_outstanding'])

    def get_yield(self):
        return float(str(self.data['yield'][:-1]))

    def get_tenor(self):
        return float(str(self.data['tenor']).replace(' years', ''))

    def get_id(self):
        return str(self.data['id'])

    def get_type(self):
        return str(self.data['type'])

    def get_data(self):
        return self.data


def has_null_value(bond):
    """
    If bond contains any null parameter return a boolean False othewise True
    :param bond: Dict
    :return: boolean True or False
    """
    for val in bond.values():
        if val is None:
            return True

    return False


def find_closest_govt_bond(govt_bond_dict, tenor):
    """
    Method to find government bond for a particular corporate bond with nearest tenor value.
    If yield values are same, then return bond with highest amountoutstanding value
    :param govt_bond_dict: dict
    :param tenor: float
    :return: Government Bond object
    """
    lst = []
    for x in govt_bond_dict.keys():
        lst.append(float(x))

    closest_tenor_value = lst[min(range(len(lst)), key=lambda i: abs(lst[i] - tenor))]
    lst_govt_bonds = govt_bond_dict[closest_tenor_value]
    govt_bond = lst_govt_bonds[0]  # Assume first bond is selected
    for bond in lst_govt_bonds:
        if govt_bond.get_amount_outstanding() < bond.get_amount_outstanding():
            govt_bond = bond

    return govt_bond, closest_tenor_value


def find_spread(govt_bond, corp_bond):
    """
    Spread is defined as the difference between the yield of a corporate bond and its government bond benchmark
    :param govt_bond: Government Bond Object
    :param corp_bond: Corporate Bond Object
    :return: basis points - scale spread by 100 converting to integer (truncating trailing decimals)
    """
    return str(int(round((abs(corp_bond.get_yield() - govt_bond.get_yield())) * 100))) + " bps"


def process(data):
    corp_bond_list = []
    govt_bond_dict = {}

    for bond_dict in data['data']:
        if has_null_value(bond_dict):
            continue

        bond = Bond(bond_dict)
        if bond.get_id().startswith('c'):
            corp_bond_list.append(bond)
        elif bond.get_type() == 'government':
            tenor = bond.get_tenor()
            if tenor in govt_bond_dict:
                govt_bond_dict[tenor].append(bond)
            else:
                govt_bond_dict[tenor] = [bond]

    output_dict = {}
    output_dict['data'] = []
    for corp_bond in corp_bond_list:
        record = {}
        govt_bond, closest_tenor = find_closest_govt_bond(govt_bond_dict, corp_bond.get_tenor())
        govt_bond_dict[closest_tenor].remove(govt_bond)
        if len(govt_bond_dict[closest_tenor])==0:
            govt_bond_dict.pop(closest_tenor)
        # govt_bond_dict[closest_tenor] = govt_bond_dict[closest_tenor].remove(govt_bond)

        record["corporate_bond_id"] = corp_bond.get_id()
        record["government_bond_id"] = govt_bond.get_id()
        record["spread_to_benchmark"] = find_spread(govt_bond, corp_bond)

        output_dict['data'].append(record)

    return output_dict


if __name__ == '__main__':

    # Take input arguments for input and output json files
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Reading file into a json dictionary
    with open(input_file) as f:
        data = json.load(f)

    output_dict = process(data)

    # Serializing json
    json_object = json.dumps(output_dict, indent=3)

    # Writing to sample_output.json
    with open(output_file, "w") as outfile:
        outfile.write(json_object)
