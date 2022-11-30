import json
from urllib.parse import urlparse
from collections import Counter, defaultdict



def jloadfunc(filepath):
    with open(filepath, encoding='utf-8-sig') as f:
        data = json.load(f)
    return data


def rubrics_iterator(jsondict, pathdict):
    dctlist = jsondict.get('rubrics', '')
    result = []
    for i in dctlist:
        rubric = i.get('name', '')
        result.append(rubric)
    pathdict['rubrics'] = result


def adm_div_iterator(jsondict, pathdict):
    dctlist = jsondict.get('adm_div', '')
    new_dict = dict()
    for i in dctlist:
        new_dict[i.get('type', '')] = i.get('name', '')
    pathdict['country'] = new_dict.get('country', '')
    pathdict['city'] = new_dict.get('city', '')


def whatsappphone_extractor(str):
    u = urlparse(str)
    phone = '+' + u.path[1:]
    return phone


def manage_duplicates(pairs):
    d = {}
    k_counter = Counter(defaultdict(int))
    for k, v in pairs:
        d[k + ' ' + str(k_counter[k] + 1)] = v
        k_counter[k] += 1
    return d


def contacts_iterator(jsondict, pathdict):
    dctlist = jsondict.get('contact_groups', '')
    tuple_list = []
    for i in dctlist:
        for x in i:
            endlist = i.get(x, '')
            for d in endlist:
                if d.get('type', '') == 'website':
                    k = d.get('type', '')
                    v = d.get('url', '')
                    tuple_list.append((k, v))
                elif d.get('type', '') == 'whatsapp':
                    k = d.get('type', '')
                    v_long = d.get('value', '')
                    v = whatsappphone_extractor(v_long)
                    tuple_list.append((k, v))
                else:
                    k = d.get('type', '')
                    v = d.get('value', '')
                    tuple_list.append((k, v))
    new_dict = manage_duplicates(tuple_list)
    for i in new_dict:
        pathdict[i] = new_dict.get(i, '')


def url_generator(jsondict, pathdict):
    json_id = jsondict['id']
    url_id = json_id.split('_', 1)[0]
    url_beginning = 'https://2gis.com/firm/'
    url = url_beginning + url_id
    pathdict['2GIS URL'] = url


def json_processer(filepath):
    data = jloadfunc(filepath)
    datalist = []
    for i in data:
        dct = dict()
        dct['organization id'] = 'ID' + i['org'].get('id', '')
        dct['branch count'] = i['org'].get('branch_count', '')
        dct['name'] = i['org'].get('name', '')
        dct['description'] = i['name_ex'].get('extension', '')
        rubrics_iterator(i, dct)
        dct['address name'] = i.get('address_name', '')
        adm_div_iterator(i, dct)
        contacts_iterator(i, dct)
        url_generator(i, dct)
        datalist.append(dct)
        res_lst = list({dct['2GIS URL']: dct for dct in datalist}.values())
    return res_lst
