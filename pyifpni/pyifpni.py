# -*- coding:utf-8 -*-
import datetime
import math
import time
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
from tqdm import tqdm
import ydata_profiling as yp


def save_to_csv(df, csv_file_path):
    df.to_csv(csv_file_path)


def html_report(df):
    return yp.ProfileReport(df)


def end():
    print("x" * 88)


def headers():
    return {"user-agent": UserAgent().random}


def plain_string(string):
    new_string = string.replace("\n", "")
    new_string = new_string.replace("\r", "")
    return new_string.strip()


def requests3(url):
    while True:
        session = requests.Session()
        try:
            res = session.get(url, headers=headers())
            if res.status_code == 200:
                return res
            else:
                time.sleep(3)
        except Exception as e:
            print('%s. You can shut down current session or script will try again after 3 seconds.' % e)
            break
        finally:
            session.close()


class IFPNI:
    def __init__(self):
        self.__url_base = "http://ifpni.org/"
        self.__url_end = ".htm?formIndex=def&submitForm=Search&isExtended=1"
        self.__form = {"Name": "", "searchOnlyByFirstSymbols": "", "sort by": {"order": "", "orderDirection": ""},
                       "extended search": {"author": "", "original spelling": "", "yearFrom": "", "yearTo": "",
                                           "rank": [], "paleoregion": [], "journal": "", "abbreviation": ""}}
        self.__rank_supragenus = {"Regnum": 2, "Subregnum": 3, "Phylum": 5, "Subphylum": 6, "Superphylum": 7,
                                  "Class": 9, "Subclass": 10, "Superclass": 11, "Infraclass": 12, "Order": 66,
                                  "Superorder": 14, "Suborder": 15, "Infraorder": 16, "Family": 18, "Superfamily": 19,
                                  "Subfamily": 20, "Infrafamily": 21, "Tribe": 23, "Supertribe": 24,
                                  "Supersubtribe": 25,
                                  "Subtribe": 26, "Infratribe": 27, "Turma": 67, "Anteturma": 29, "Suprasubturma": 30,
                                  "Subturma": 31, "Infraturma": 32, "Unranked": 59}
        self.__rank_genus = {"Genus": 68, "Supergenus": 43, "Group": 69, "Subgroup": 45, "Unranked": 56}
        self.__rank_infragenus = {"Genus": 70, "Infragenus": 47, "Subgenus": 48, "Section": 49, "Subsection": 50,
                                  "Supersection": 51, "Series": 52, "Subseries": 53, "Superseries": 54, "Unranked": 55}
        self.__rank_species = {"Species": 33, "Superspecies": 34, "Unranked": 58}
        self.__rank_infraspecies = {"Subspecies": 35, "Supervarietas": 36, "Varietas": 37, "Subvarietas": 38,
                                    "Forma": 39, "Subforma": 40, "Infraspecies": 41, "Unranked": 57}
        self.__paleoregion = {"Africa": 1, "Africa (East)": 2, "Africa (Equatorial)": 3, "Africa (North)": 4,
                              "Africa (South)": 5, "Africa (West)": 6, "Altaida (Altaides)": 7, "Altaj": 8,
                              "America": 122, "America (Caribbean)": 9, "America (North)": 10,
                              "America (North - Greenland)": 104, "America (South)": 11, "Anatolia": 12, "Angarida": 13,
                              "Angarida (Mongolia)": 136, "Antarctica": 14, "Arctic": 15, "Australia": 16,
                              "Australia (New Zealand)": 17, "Avalonia": 18, "Baltica": 19, "Cathaysia": 20,
                              "Cathaysia (Kitakamiland)": 21, "Cathaysia (North)": 22, "Cathaysia (Sino-Korea)": 105,
                              "Cathaysia (South)": 23, "Caucasus": 24, "China (North)": 26, "China (South)": 25,
                              "Chingiz": 27, "Columbia (Amazonia)": 158, "Columbia (Australia)": 147,
                              "Columbia (Baltica)": 156, "Columbia (East Antarctica)": 159, "Columbia (Greenland)": 157,
                              "Columbia (Indostan)": 137, "Columbia (Kalahari)": 154, "Columbia (Laurentia)": 151,
                              "Columbia (North Australia)": 164, "Columbia (North China)": 155,
                              "Columbia (South Australia)": 160, "Columbia (South China)": 153,
                              "Columbia (West Africa)": 152, "Columbia (West Australia)": 161,
                              "Congo-São Francisco (Congo)": 172, "Eurasia": 28, "Eurasia (Anatolia)": 29,
                              "Eurasia (Arabian peninsula)": 30, "Eurasia (Asia)": 32, "Eurasia (Asia Minor)": 31,
                              "Eurasia (Caucasus)": 33, "Eurasia (Central Asia)": 36,
                              "Eurasia (Central Asia and Caucasus)": 34, "Eurasia (Central Asia and Urals)": 35,
                              "Eurasia (China)": 37, "Eurasia (Europe)": 41, "Eurasia (Europe & Urals)": 38,
                              "Eurasia (Europe and Central Asia)": 39, "Eurasia (Europe and W Siberia)": 40,
                              "Eurasia (Far East)": 45, "Eurasia (Far East & Central Asia)": 42,
                              "Eurasia (Far East & China)": 43, "Eurasia (Far East and Japanese Archipelago)": 44,
                              "Eurasia (Greenland)": 46, "Eurasia (Himalayas)": 47, "Eurasia (Indochina)": 48,
                              "Eurasia (Indostan)": 49, "Eurasia (Japanese Archipelago)": 51,
                              "Eurasia (Japanese Archipelago and Sakhalin)": 50, "Eurasia (Java Island)": 52,
                              "Eurasia (Maritime Southeast Asia)": 53, "Eurasia (Mesopotamian Plain)": 54,
                              "Eurasia (Middle East)": 55, "Eurasia (Novaja Zemlja Archipelago)": 56,
                              "Eurasia (S Asia)": 123, "Eurasia (S Urals)": 57, "Eurasia (SE Asia)": 58,
                              "Eurasia (Siberia)": 61, "Eurasia (Siberia and Central Asia)": 59,
                              "Eurasia (Siberia and Far East)": 60, "Eurasia (South China)": 62,
                              "Eurasia (South East)": 63, "Eurasia (Tarim Basin)": 134, "Eurasia (Tibet)": 64,
                              "Eurasia (Urals)": 65, "Eurasia (W Asia)": 66, "Eurasia (W Asia & Caucasus)": 67,
                              "Eurasia (W Siberia)": 69, "Eurasia (W Siberia & Central Asia)": 68, "Europe": 71,
                              "Europe (Cis-Caspian)": 72, "Gondwana (Africa)": 73, "Gondwana (Antarctica)": 74,
                              "Gondwana (Arabia)": 126, "Gondwana (Armorica)": 75, "Gondwana (Australia)": 76,
                              "Gondwana (Indostan)": 77, "Gondwana (N Africa)": 78,
                              "Gondwana (N Africa [Tethys palaeocean])": 79, "Gondwana (New Caledonia)": 131,
                              "Gondwana (New Zealand)": 132, "Gondwana (Perunica)": 80, "Gondwana (S America)": 81,
                              "Gondwana (Sardinia)": 113, "Gondwana (Saxo-Thuringia)": 82,
                              "Gondwana (South Africa)": 124,
                              "Gondwana (South America)": 83, "Kazakhstania": 84, "Kazakhstania (Xinjiang)": 85,
                              "Kenorland (Baltica)": 168, "Kenorland (Kalaharia)": 169, "Kenorland (Laurentia)": 167,
                              "Kenorland (Western Australia)": 170, "Kitakamiland": 86, "Laurentia": 87,
                              "Laurussia": 88,
                              "Laurussia (Anatolia)": 89, "Laurussia (Armorica)": 90, "Laurussia (Avalonia)": 93,
                              "Laurussia (Avalonia & Baltica)": 92, "Laurussia (Baltica)": 94,
                              "Laurussia (Cantabria)": 95, "Laurussia (Iberica)": 96, "Laurussia (Laurentia)": 97,
                              "Laurussia (Moesia)": 98, "Laurussia (Moldanubia)": 125, "Laurussia (Perunica)": 90,
                              "Laurussia (Rhenano-Hercynia)": 100, "Laurussia (Saxo-Thuringia)": 101, "Moldanubia": 102,
                              "Mongolia (Western)": 103, "not specified": 106, "Pacific": 107, "Pamir-Alaj": 108,
                              "Pannotia (Antarctica)": 174, "Pannotia (Indostan)": 175, "Pannotia (Siberia)": 150,
                              "Perunica": 109, "Proangarida": 110, "Rodinia": 111, "Rodinia (Amazonia)": 141,
                              "Rodinia (Australia)": 146, "Rodinia (Baltica)": 148, "Rodinia (Indostan)": 138,
                              "Rodinia (Laurentia)": 140, "Rodinia (North China)": 112, "Rodinia (Rio Plato)": 142,
                              "Rodinia (Siberia)": 149, "Rodinia (South China)": 139, "Siberia": 114, "Sibumasu": 115,
                              "Superior Craton (Superior Craton)": 171, "Tibet": 116, "Tien Shan": 117,
                              "Tien Shan (North)": 118, "Tien Shan (South)": 133, "Tuva": 119, "unknown": 120,
                              "Vaalbara (Kaapvaal)": 165, "Vaalbara (Pilbara)": 166, "Xinjiang": 121}
        self.__repository = []
        self.__result = None

    def available_rank(self, method=""):
        if method == "supragenus":
            print(f"Available rank list for supragenus:\n\t {list(self.__rank_supragenus.keys())}")
        elif method == "genus":
            print(f"Available rank list for genus:\n\t {list(self.__rank_genus.keys())}")
        elif method == "infragenus":
            print(f"Available rank list for infragenus:\n\t {list(self.__rank_infragenus.keys())}")
        elif method == "species":
            print(f"Available rank list for species:\n\t {list(self.__rank_species.keys())}")
        elif method == "infraspecies":
            print(f"Available rank list for infraspecies:\n\t {list(self.__rank_infraspecies.keys())}")
        else:
            print(f"Available rank list for supragenus:\n\t {list(self.__rank_supragenus.keys())}")
            print(f"Available rank list for genus:\n\t {list(self.__rank_genus.keys())}")
            print(f"Available rank list for infragenus:\n\t {list(self.__rank_infragenus.keys())}")
            print(f"Available rank list for species:\n\t {list(self.__rank_species.keys())}")
            print(f"Available rank list for infraspecies:\n\t {list(self.__rank_infraspecies.keys())}")

    def available_paleoregion(self):
        print(f"Available paleoregion list: \n\t {list(self.__paleoregion.keys())}")

    def __set_form(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                   original_spelling=None, yearFrom=None, yearTo=None, rank_list=None, paleoregion_list=None,
                   journal=None, abbreviation=None):
        self.__form["Name"] = name
        if first_symbols and isinstance(first_symbols, bool):
            self.__form["searchOnlyByFirstSymbols"] = "on"
        if order and orderDirection and isinstance(order, str) and isinstance(orderDirection, str):
            self.__form["sort by"]["order"] = order
            self.__form["sort by"]["orderDirection"] = orderDirection
        if author and isinstance(author, str):
            self.__form["extended search"]["author"] = author
        if original_spelling and isinstance(original_spelling, str):
            self.__form["extended search"]["original spelling"] = original_spelling
        if yearFrom and (isinstance(yearFrom, str) or isinstance(yearFrom, int)):
            try:
                if int(yearFrom) >= 1753:
                    self.__form["extended search"]["yearFrom"] = str(yearFrom)
            except ValueError:
                pass
        if yearTo and (isinstance(yearTo, str) or isinstance(yearTo, int)):
            try:
                year = datetime.datetime.today().year
                if int(yearTo) <= year:
                    self.__form["extended search"]["yearTo"] = str(yearTo)
            except ValueError:
                pass
        if rank_list and isinstance(rank_list, list):
            self.__form["extended search"]["rank"] = rank_list
        if paleoregion_list and isinstance(paleoregion_list, list):
            self.__form["extended search"]["paleoregion"] = paleoregion_list
        if journal and isinstance(journal, str):
            self.__form["extended search"]["journal"] = journal
        if abbreviation and isinstance(abbreviation, str):
            self.__form["extended search"]["abbreviation"] = abbreviation

    def __merge_url(self, method):
        url = ''.join([self.__url_base, method, self.__url_end])
        tem_list = [url]
        if method == "name":
            return url
        elif method in ["supragenus", "genus", "infragenus", "species", "infraspecies"]:
            tem_list.append("name=%s" % self.__form["Name"])
            tem_list.append("searchOnlyByFirstSymbols=%s" % self.__form["searchOnlyByFirstSymbols"])
            tem_list.append("order=%s" % self.__form["sort by"]["order"])
            tem_list.append("orderDirection=%s" % self.__form["sort by"]["orderDirection"])
            tem_list.append("author=%s" % self.__form["extended search"]["author"])
            tem_list.append("titleOrig=%s" % self.__form["extended search"]["original spelling"])
            tem_list.append("yearFrom=%s" % self.__form["extended search"]["yearFrom"])
            tem_list.append("yearTo=%s" % self.__form["extended search"]["yearTo"])
            if method == "supragenus":
                for rank in self.__form["extended search"]["rank"]:
                    tem_list.append("rankID[]=%i" % self.__rank_supragenus[rank])
                return '&'.join(tem_list)
            elif method == "genus":
                for rank in self.__form["extended search"]["rank"]:
                    tem_list.append("rankID[]=%i" % self.__rank_genus[rank])
                return '&'.join(tem_list)
            elif method == "infragenus":
                for rank in self.__form["extended search"]["rank"]:
                    tem_list.append("rankID[]=%i" % self.__rank_infragenus[rank])
                return '&'.join(tem_list)
            elif method == "species":
                for rank in self.__form["extended search"]["rank"]:
                    tem_list.append("rankID[]=%i" % self.__rank_species[rank])
                for pr in self.__form["extended search"]["paleoregion"]:
                    tem_list.append("paleoID=%i" % self.__paleoregion[pr])
                return '&'.join(tem_list)
            else:
                for rank in self.__form["extended search"]["rank"]:
                    tem_list.append("rankID[]=%i" % self.__rank_infraspecies[rank])
                for pr in self.__form["extended search"]["paleoregion"]:
                    tem_list.append("paleoID=%i" % self.__paleoregion[pr])
                return '&'.join(tem_list)
        elif method in ["publication", "book", "journal"]:
            tem_list.append("title=%s" % self.__form["Name"])
            tem_list.append("searchOnlyByFirstSymbols=%s" % self.__form["searchOnlyByFirstSymbols"])
            tem_list.append("order=%s" % self.__form["sort by"]["order"])
            tem_list.append("orderDirection=%s" % self.__form["sort by"]["orderDirection"])
            if method == "publication":
                tem_list.append("author=%s" % self.__form["extended search"]["author"])
                tem_list.append("titleOrig=%s" % self.__form["extended search"]["original spelling"])
                tem_list.append("yearFrom=%s" % self.__form["extended search"]["yearFrom"])
                tem_list.append("yearTo=%s" % self.__form["extended search"]["yearTo"])
                tem_list.append("journalID=%s" % self.__form["extended search"]["journal"])
                return '&'.join(tem_list)
            elif method == "book":
                tem_list.append("titleOrig=%s" % self.__form["extended search"]["original spelling"])
                tem_list.append("titleAbbr=%s" % self.__form["extended search"]["abbreviation"])
                return '&'.join(tem_list)
            else:
                tem_list.append("titleOrig=%s" % self.__form["extended search"]["original spelling"])
                tem_list.append("yearFrom=%s" % self.__form["extended search"]["yearFrom"])
                tem_list.append("yearTo=%s" % self.__form["extended search"]["yearTo"])
                return '&'.join(tem_list)
        else:
            tem_list.append("lastName=%s" % self.__form["Name"])
            tem_list.append("searchOnlyByFirstSymbols=%s" % self.__form["searchOnlyByFirstSymbols"])
            tem_list.append("order=%s" % self.__form["sort by"]["order"])
            tem_list.append("orderDirection=%s" % self.__form["sort by"]["orderDirection"])
            return '&'.join(tem_list)

    def __method_to_url(self, method, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                        original_spelling=None, yearFrom=None, yearTo=None, rank_list=None, paleoregion_list=None,
                        journal=None, abbreviation=None):
        if isinstance(method, str):
            self.__set_form(name, first_symbols, order, orderDirection, author, original_spelling, yearFrom, yearTo,
                            rank_list, paleoregion_list, journal, abbreviation)
        return self.__merge_url(method)

    def __basic_to_method(self, url, method):
        result2df = None
        res = requests3(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        total_count_num = soup.find("div", class_="list-group").find("h4").text.split(' ')[-1]
        total_page_num = math.ceil(int(total_count_num) / 10)
        print(f"There is/are {total_count_num} result(s) founded on {total_page_num} page(s).")
        for page in range(1, total_page_num + 1):
            tem_url = "&".join([url, "page=%i" % page])
            tem_res = requests3(tem_url)
            tem_soup = BeautifulSoup(tem_res.text, "html.parser")
            list_group_item = tem_soup.find("div", class_="list-group").find_all("span", class_="list-group-item")
            items = tqdm(list_group_item)
            for item in items:
                items.set_description(f"\t|______ executing page {page}: {len(list_group_item)} items.")
                tem_item = {}
                try:
                    if method in ['supragenus', 'genus', 'infragenus', 'species', 'infraspecies']:
                        tem_item["href"] = self.__url_base + item.find("h1").find("a")["href"]
                    else:
                        tem_item["href"] = self.__url_base + item["href"]
                except TypeError:
                    pass
                info_res = requests3(tem_item["href"])
                info_soup = BeautifulSoup(info_res.text, 'html.parser')
                head = info_soup.find("span", class_="input-group-addon label label-info")
                tem_item[head.text] = plain_string(head.find_next("span").text)
                dl = info_soup.find("dl", class_="dl-horizontal")
                for i in dl.find_all("dt"):
                    column_label = i.text.strip()
                    column_value = i.find_next("dd")
                    try:
                        tem_item[column_label] = plain_string(column_value.text)
                        tem_item[column_label + ' href'] = self.__url_base + column_value.find('a')['href']
                    except TypeError:
                        tem_item[column_label] = plain_string(column_value.text)
                result2df = pd.concat([result2df, pd.DataFrame.from_dict(tem_item, orient="index").T],
                                      ignore_index=True)
                self.__result = pd.concat([self.__result, pd.DataFrame.from_dict(tem_item, orient="index").T],
                                          ignore_index=True)
        end()
        return result2df

    def supragenus(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                   original_spelling=None, yearFrom=None, yearTo=None, rank_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m supragenus \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="supragenus", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list)
        return self.__basic_to_method(url, method="supragenus")

    def genus(self, name="", first_symbols=False, order=None, orderDirection=None, author=None, original_spelling=None,
              yearFrom=None, yearTo=None, rank_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m genus \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="genus", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list)
        return self.__basic_to_method(url, method="genus")

    def infragenus(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                   original_spelling=None, yearFrom=None, yearTo=None, rank_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m infragenus \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="infragenus", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list)
        return self.__basic_to_method(url, method="infragenus")

    def species(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                original_spelling=None, yearFrom=None, yearTo=None, rank_list=None, paleoregion_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m species \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="species", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list,
                                   paleoregion_list=paleoregion_list)
        return self.__basic_to_method(url, method="species")

    def infraspecies(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                     original_spelling=None, yearFrom=None, yearTo=None, rank_list=None, paleoregion_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m infraspecies \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="infraspecies", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list,
                                   paleoregion_list=paleoregion_list)
        return self.__basic_to_method(url, method="infraspecies")

    def publication(self, title="", first_symbols=False, order=None, orderDirection=None, author=None,
                    original_spelling=None, yearFrom=None, yearTo=None, journal=None):
        print('-' * 20 + 'Proceeding \033[1;32m publication \033[0m (based on publication) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {title}\033[0m')
        url = self.__method_to_url(method="publication", name=title, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, journal=journal)
        return self.__basic_to_method(url, method="publication")

    def book(self, title="", first_symbols=False, order=None, orderDirection=None, original_spelling=None,
             abbreviation=None):
        print('-' * 20 + 'Proceeding \033[1;32m book \033[0m (based on publication) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {title}\033[0m')
        url = self.__method_to_url(method="book", name=title, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, original_spelling=original_spelling,
                                   abbreviation=abbreviation)
        return self.__basic_to_method(url, method="book")

    def journal(self, title="", first_symbols=False, order=None, orderDirection=None, original_spelling=None,
                yearFrom=None, yearTo=None):
        print('-' * 20 + 'Proceeding \033[1;32m journal \033[0m (based on publication) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {title}\033[0m')
        url = self.__method_to_url(method="journal", name=title, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo)
        return self.__basic_to_method(url, method="journal")

    def author(self, lastName="", first_symbols=False, order=None, orderDirection=None):
        print('-' * 20 + 'Proceeding \033[1;32m author \033[0m (based on publication) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {lastName}\033[0m')
        url = self.__method_to_url(method="author", name=lastName, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection)
        return self.__basic_to_method(url, method="author")

    def __find_ancestors_taxonomic(self, basic_df):
        self.__result = None
        for row in basic_df.itertuples(index=False):
            self.__repository = []
            print(f"\n**Current fossil plant name is \033[32m{row.Name}\033[0m**")
            self.__find_ancestors_taxonomic_iterator(row.href)
        end()
        return self.__result

    def __find_ancestors_taxonomic_iterator(self, href, prefix='\t'):
        prefix += '\t'
        if href not in self.__repository:
            self.__repository.append(href)
            tem_item = {'href': href}
            info_res = requests3(tem_item["href"])
            info_soup = BeautifulSoup(info_res.text, 'html.parser')
            head = info_soup.find("span", class_="input-group-addon label label-info")
            tem_item[head.text] = head.find_next("span").text
            dl = info_soup.find("dl", class_="dl-horizontal")
            report = info_soup.find("div", id="nomenQuote").text
            print("%s|____ %s" % (prefix, plain_string(report)))
            for i in dl.find_all("dt"):
                column_label = i.text.strip()
                column_value = i.find_next("dd")
                try:
                    tem_item[column_label] = plain_string(column_value.text)
                    tem_item[column_label + ' href'] = self.__url_base + column_value.find('a')['href']
                except TypeError:
                    tem_item[column_label] = plain_string(column_value.text)
            self.__result = pd.concat([self.__result, pd.DataFrame.from_dict(tem_item, orient="index").T],
                                      ignore_index=True)
            try:
                try:
                    self.__find_ancestors_taxonomic_iterator(tem_item["Parent Taxon href"], prefix)
                except KeyError:
                    try:
                        self.__find_ancestors_taxonomic_iterator(tem_item["Generic Name href"], prefix)
                    except KeyError:
                        self.__find_ancestors_taxonomic_iterator(tem_item['Species href'], prefix)
            except KeyError:
                pass

    def supragenus_ancestors(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                             original_spelling=None, yearFrom=None, yearTo=None, rank_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m ancestors of supragenus \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="supragenus", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list)
        basic_df = self.__basic_to_method(url, method="supragenus")
        return self.__find_ancestors_taxonomic(basic_df)

    def genus_ancestors(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                        original_spelling=None, yearFrom=None, yearTo=None, rank_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m ancestors of genus \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="genus", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list)
        basic_df = self.__basic_to_method(url, method="genus")
        return self.__find_ancestors_taxonomic(basic_df)

    def infragenus_ancestors(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                             original_spelling=None, yearFrom=None, yearTo=None, rank_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m ancestors of infragenus \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="infragenus", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list)
        basic_df = self.__basic_to_method(url, method="infragenus")
        return self.__find_ancestors_taxonomic(basic_df)

    def species_ancestors(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                          original_spelling=None, yearFrom=None, yearTo=None, rank_list=None, paleoregion_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m ancestors of species \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="species", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list,
                                   paleoregion_list=paleoregion_list)
        basic_df = self.__basic_to_method(url, method="species")
        return self.__find_ancestors_taxonomic(basic_df)

    def infraspecies_ancestors(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                               original_spelling=None, yearFrom=None, yearTo=None, rank_list=None,
                               paleoregion_list=None):
        print(
            '-' * 20 + 'Proceeding \033[1;32m ancestors of infraspecies \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="infraspecies", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list,
                                   paleoregion_list=paleoregion_list)
        basic_df = self.__basic_to_method(url, method="infraspecies")
        return self.__find_ancestors_taxonomic(basic_df)

    def __find_descendants_taxonomic(self, basic_df):
        self.__result = None
        try:
            for row in basic_df.itertuples(index=False):
                self.__repository = []
                try:
                    print(f"\n**Current fossil plant name is \033[32m{row.Name}\033[0m**")
                except AttributeError:
                    print(f"A non-plant group name is skipped, which could be a journal, book, or publication.")
                self.__find_descendants_taxonomic_iterator(row.href)
        except AttributeError:
            pass
        end()
        return self.__result

    def __find_descendants_taxonomic_iterator(self, href, prefix='\t'):
        prefix += '\t'
        if href not in self.__repository:
            self.__repository.append(href)
            tem_item = {'href': href}
            info_res = requests3(tem_item["href"])
            info_soup = BeautifulSoup(info_res.text, 'html.parser')
            head = info_soup.find("span", class_="input-group-addon label label-info")
            tem_item[head.text] = head.find_next("span").text
            dl = info_soup.find("dl", class_="dl-horizontal")
            report = info_soup.find("div", id="nomenQuote").text
            print("%s|____ %s" % (prefix, plain_string(report)))
            for i in dl.find_all("dt"):
                column_label = i.text.strip()
                column_value = i.find_next("dd")
                try:
                    tem_item[column_label] = plain_string(column_value.text)
                    tem_item[column_label + ' href'] = self.__url_base + column_value.find('a')['href']
                except TypeError:
                    tem_item[column_label] = plain_string(column_value.text)
            self.__result = pd.concat([self.__result, pd.DataFrame.from_dict(tem_item, orient="index").T],
                                      ignore_index=True)
            try:
                for i in info_soup.find("div", class_="dopLinksForItem").find_all("div", class_="linkForItem"):
                    self.__find_descendants_taxonomic_iterator(self.__url_base + i.find("a")['href'], prefix)
            except AttributeError:
                pass

    def supragenus_descendants(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                               original_spelling=None, yearFrom=None, yearTo=None, rank_list=None):
        print(
            '-' * 20 + 'Proceeding \033[1;32m descendants of supragenus \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="supragenus", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list)
        basic_df = self.__basic_to_method(url, method="supragenus")
        return self.__find_descendants_taxonomic(basic_df)

    def genus_descendants(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                          original_spelling=None, yearFrom=None, yearTo=None, rank_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m descendants of genus \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="genus", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list)
        basic_df = self.__basic_to_method(url, method="genus")
        return self.__find_descendants_taxonomic(basic_df)

    def infragenus_descendants(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                               original_spelling=None, yearFrom=None, yearTo=None, rank_list=None):
        print(
            '-' * 20 + 'Proceeding \033[1;32m descendants of infragenus \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="infragenus", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list)
        basic_df = self.__basic_to_method(url, method="infragenus")
        return self.__find_descendants_taxonomic(basic_df)

    def species_descendants(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                            original_spelling=None, yearFrom=None, yearTo=None, rank_list=None, paleoregion_list=None):
        print('-' * 20 + 'Proceeding \033[1;32m descendants of species \033[0m (based on taxonomic) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="species", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list,
                                   paleoregion_list=paleoregion_list)
        basic_df = self.__basic_to_method(url, method="species")
        return self.__find_descendants_taxonomic(basic_df)

    def infraspecies_descendants(self, name="", first_symbols=False, order=None, orderDirection=None, author=None,
                                 original_spelling=None, yearFrom=None, yearTo=None, rank_list=None,
                                 paleoregion_list=None):
        print(
            '-' * 20 + 'Proceeding \033[1;32m descendants of infraspecies \033[0m (based on taxonomic) method' + '-' *
            20)
        print(f'\033[1;34mSearching about: {name}\033[0m')
        url = self.__method_to_url(method="infraspecies", name=name, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, rank_list=rank_list,
                                   paleoregion_list=paleoregion_list)
        basic_df = self.__basic_to_method(url, method="infraspecies")
        return self.__find_descendants_taxonomic(basic_df)

    def __find_taxon_publication(self, basic_df, prefix='\t', next_level=False):
        self.__result = None
        for row in basic_df.itertuples(index=False):
            self.__repository = []
            try:
                print(f"\n**Current publication name is \033[32m{row.Title}\033[0m**")
            except AttributeError:
                print(f"Current session:")
            href = row.href
            prefix += '\t'
            if href not in self.__repository:
                self.__repository.append(href)
                tem_item = {'href': href}
                info_res = requests3(tem_item["href"])
                info_soup = BeautifulSoup(info_res.text, 'html.parser')
                head = info_soup.find("span", class_="input-group-addon label label-info")
                tem_item[head.text] = head.find_next("span").text
                dl = info_soup.find("dl", class_="dl-horizontal")
                report = info_soup.find("div", class_="panel-body").find("h1").text
                print("%s|____ %s" % (prefix, plain_string(report)))
                for i in dl.find_all("dt"):
                    column_label = i.text.strip()
                    column_value = i.find_next("dd")
                    try:
                        tem_item[column_label] = plain_string(column_value.text)
                        tem_item[column_label + ' href'] = self.__url_base + column_value.find('a')['href']
                    except TypeError:
                        tem_item[column_label] = plain_string(column_value.text)
                self.__result = pd.concat([self.__result, pd.DataFrame.from_dict(tem_item, orient="index").T],
                                          ignore_index=True)
                try:
                    for i1 in info_soup.find("div", class_="dopLinksForItem").find_all("div", class_="linkForItem"):
                        tem_item = {'href': self.__url_base + i1.find("a")['href']}
                        info_res = requests3(tem_item["href"])
                        info_soup = BeautifulSoup(info_res.text, 'html.parser')
                        head = info_soup.find("span", class_="input-group-addon label label-info")
                        tem_item[head.text] = head.find_next("span").text
                        dl = info_soup.find("dl", class_="dl-horizontal")
                        report = info_soup.find("div", class_="panel-body").find("h1").text
                        print("%s|____ %s" % (prefix + '\t', plain_string(report)))
                        for i2 in dl.find_all("dt"):
                            column_label = i2.text.strip()
                            column_value = i2.find_next("dd")
                            try:
                                tem_item[column_label] = plain_string(column_value.text)
                                tem_item[column_label + ' href'] = self.__url_base + column_value.find('a')['href']
                            except TypeError:
                                tem_item[column_label] = plain_string(column_value.text)
                        self.__result = pd.concat([self.__result, pd.DataFrame.from_dict(tem_item, orient="index").T],
                                                  ignore_index=True)
                        if next_level:
                            for i3 in info_soup.find("div", class_="dopLinksForItem").find_all("div",
                                                                                               class_="linkForItem"):
                                tem_item = {'href': self.__url_base + i3.find("a")['href']}
                                info_res = requests3(tem_item["href"])
                                info_soup = BeautifulSoup(info_res.text, 'html.parser')
                                head = info_soup.find("span", class_="input-group-addon label label-info")
                                tem_item[head.text] = head.find_next("span").text
                                dl = info_soup.find("dl", class_="dl-horizontal")
                                report = info_soup.find("div", class_="panel-body").find("h1").text
                                print("%s|____ %s" % (prefix + '\t\t', plain_string(report)))
                                for i4 in dl.find_all("dt"):
                                    column_label = i4.text.strip()
                                    column_value = i4.find_next("dd")
                                    try:
                                        tem_item[column_label] = plain_string(column_value.text)
                                        tem_item[column_label + ' href'] = self.__url_base + column_value.find('a')[
                                            'href']
                                    except TypeError:
                                        tem_item[column_label] = plain_string(column_value.text)
                                self.__result = pd.concat(
                                    [self.__result, pd.DataFrame.from_dict(tem_item, orient="index").T],
                                    ignore_index=True)
                except AttributeError:
                    pass
        end()
        return self.__result

    def publication2taxon(self, title="", first_symbols=False, order=None, orderDirection=None, author=None,
                          original_spelling=None, yearFrom=None, yearTo=None, journal=None):
        print(
            '-' * 20 + 'Proceeding \033[1;32m taxon names of publication \033[0m (based on publication) method' + '-' *
            20)
        print(f'\033[1;34mSearching about: {title}\033[0m')
        url = self.__method_to_url(method="publication", name=title, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo, journal=journal)
        basic_df = self.__basic_to_method(url, method="publication")
        return self.__find_taxon_publication(basic_df)

    def book2taxon(self, title="", first_symbols=False, order=None, orderDirection=None, original_spelling=None,
                   abbreviation=None):
        print('-' * 20 + 'Proceeding \033[1;32m taxon names of book \033[0m (based on publication) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {title}\033[0m')
        url = self.__method_to_url(method="book", name=title, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, original_spelling=original_spelling,
                                   abbreviation=abbreviation)
        basic_df = self.__basic_to_method(url, method="book")
        return self.__find_taxon_publication(basic_df, next_level=True)

    def journal2taxon(self, title="", first_symbols=False, order=None, orderDirection=None, original_spelling=None,
                      yearFrom=None, yearTo=None):
        print(
            '-' * 20 + 'Proceeding \033[1;32m taxon names of journal \033[0m (based on publication) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {title}\033[0m')
        url = self.__method_to_url(method="journal", name=title, first_symbols=first_symbols, order=order,
                                   orderDirection=orderDirection, original_spelling=original_spelling,
                                   yearFrom=yearFrom, yearTo=yearTo)
        basic_df = self.__basic_to_method(url, method="journal")
        return self.__find_taxon_publication(basic_df, next_level=True)

    def author2publication(self, lastName="", first_symbols=False, order=None, orderDirection=None):
        print('-' * 20 + 'Proceeding \033[1;32m publication of author \033[0m (based on author) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {lastName}\033[0m')
        result = None
        try:
            # result = self.publication(author=lastName, first_symbols=first_symbols, order=order,
                                      # orderDirection=orderDirection)
            url = self.__method_to_url(method="publication", first_symbols=first_symbols, order=order,
                                       orderDirection=orderDirection, author=lastName)
            result = self.__basic_to_method(url, method="publication")
        except AttributeError:
            pass
        finally:
            return result

    def author2taxon(self, lastName="", first_symbols=False, order=None, orderDirection=None):
        self.__result = None
        print('-' * 20 + 'Proceeding \033[1;32m taxon names of author \033[0m (based on author) method' + '-' * 20)
        print(f'\033[1;34mSearching about: {lastName}\033[0m')
        try:
            self.supragenus(author=lastName, first_symbols=first_symbols, order=order, orderDirection=orderDirection)
        except AttributeError:
            pass
        try:
            self.genus(author=lastName, first_symbols=first_symbols, order=order, orderDirection=orderDirection)
        except AttributeError:
            pass
        try:
            self.infragenus(author=lastName, first_symbols=first_symbols, order=order, orderDirection=orderDirection)
        except AttributeError:
            pass
        try:
            self.species(author=lastName, first_symbols=first_symbols, order=order, orderDirection=orderDirection)
        except AttributeError:
            pass
        try:
            self.infraspecies(author=lastName, first_symbols=first_symbols, order=order, orderDirection=orderDirection)
        except AttributeError:
            pass
        return self.__result


if __name__ == "__main__":
    ifpni = IFPNI()

    # passed tests
    #ifpni.available_rank()
    #ifpni.availalbe_rank(method="supragenus")
    #ifpni.available_paleoregion()

    #orchi = ifpni.supragenus(name="Orchidaceae")
    #ach = ifpni.genus(name="achlys")
    #sph = ifpni.infragenus(name="Sphenopteris")
    #cor = ifpni.species(name="Cordaites")
    #lop = ifpni.infraspecies(name="Lophozonotriletes")

    #o2a = ifpni.supragenus_ancestors(name="orchidaceae")
    #a2a = ifpni.genus_ancestors(name="achlys")
    #s2a = ifpni.infragenus_ancestors(name="Stratiotes Imperfectus")
    #c2a = ifpni.species_ancestors(name="Cordaites acadianus")
    #p2a = ifpni.infraspecies_ancestors(name="Populus balsamoides minor")

    #o2d = ifpni.supragenus_descendants(name='orchidaceae')
    #a2d = ifpni.genus_descendants(name='alloberberis')
    #g2d = ifpni.infragenus_descendants(name="Gleicheniidites Triplexisporis")
    #c2d = ifpni.species_descendants(name='Cordaites acadianus')
    #p2d = ifpni.infraspecies_descendants(name='Populus balsamoides minor')

    #p = ifpni.publication(title="Proposal to conserve the name")
    #b = ifpni.book(title="Beiträge zur Kenntniss der fossilen Flora")
    #j = ifpni.journal(title="Acta Palaeontologica")
    #abr = ifpni.author(lastName="Abramova")

    #p2t = ifpni.publication2taxon(title='A brief review of the stratigraphy and floral succession of the Carboniferous in NW. Spain')
    #j2t = ifpni.book2taxon(title='100 Jahre Arboretum Berlin')
    #a2t = ifpni.journal2taxon(title="Acta Palaeontologica Polonica")

    #a2p = ifpni.author2publication(lastName='Abramova')
    #a2t = ifpni.author2taxon(lastName='Abramova')

    #print(a2t)

