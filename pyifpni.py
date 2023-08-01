import math
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class pyIFPNI:
    def __init__(self):
        self.url_base = "http://ifpni.org/"
        self.url_end = ".htm?formIndex=def&submitForm=Search&isExtended=1"
        self.lists_lists = {"name": "name",
                            "supragenus": "supragenus",
                            "genus": "genus",
                            "infragenus": "infragenus",
                            "species": "species",
                            "infraspecies": "infraspecies",
                            "publication": "publication",
                            "book": "book",
                            "journal": "journal",
                            "author": "author"}
        self.lists = ""
        self.form = {"Name": "",
                     "searchOnlyByFirstSymbols": "",
                     "sort by": {"order": "",
                                 "orderDirection": ""},
                     "extended search": {"author": "",
                                         "original spelling": "",
                                         "yearFrom": "",
                                         "yearTo": "",
                                         "rank": [],
                                         "paleoregion": [],
                                         "journal": "",
                                         "abbreviation": ""}
                     }
        self.rank_supragenus = {"Regnum": 2, "Subregnum": 3, "Phylum": 5, "Subphylum": 6, "Superphylum": 7,
                                "Class": 9, "Subclass": 10, "Superclass": 11, "Infraclass": 12, "Order": 66,
                                "Superorder": 14, "Suborder": 15, "Infraorder": 16, "Family": 18, "Superfamily": 19,
                                "Subfamily": 20, "Infrafamily": 21, "Tribe": 23, "Supertribe": 24, "Supersubtribe": 25,
                                "Subtribe": 26, "Infratribe": 27, "Turma": 67, "Anteturma": 29, "Suprasubturma": 30,
                                "Subturma": 31, "Infraturma": 32, "Unranked": 59}
        self.rank_genus = {"Genus": 68, "Supergenus": 43, "Group": 69, "Subgroup": 45, "Unranked": 56}
        self.rank_infragenus = {"Genus": 70, "Infragenus": 47, "Subgenus": 48, "Section": 49, "Subsection": 50,
                                "Supersection": 51, "Series": 52, "Subseries": 53, "Superseries": 54, "Unranked": 55}
        self.rank_species = {"Species": 33, "Superspecies": 34, "Unranked": 58}
        self.rank_infraspecies = {"Subspecies": 35, "Supervarietas": 36, "Varietas": 37, "Subvarietas": 38,
                                  "Forma": 39, "Subforma": 40, "Infraspecies": 41, "Unranked": 57}
        self.paleoregion = {"Africa": 1, "Africa (East)": 2, "Africa (Equatorial)": 3, "Africa (North)": 4,
                            "Africa (South)": 5, "Africa (West)": 6, "Altaida (Altaides)": 7, "Altaj": 8,
                            "America": 122, "America (Caribbean)": 9, "America (North)": 10,
                            "America (North - Greenland)": 104, "America (South)": 11, "Anatolia": 12,
                            "Angarida": 13, "Angarida (Mongolia)": 136, "Antarctica": 14, "Arctic": 15,
                            "Australia": 16, "Australia (New Zealand)": 17, "Avalonia": 18, "Baltica": 19,
                            "Cathaysia": 20, "Cathaysia (Kitakamiland)": 21, "Cathaysia (North)": 22,
                            "Cathaysia (Sino-Korea)": 105, "Cathaysia (South)": 23, "Caucasus": 24,
                            "China (North)": 26, "China (South)": 25, "Chingiz": 27, "Columbia (Amazonia)": 158,
                            "Columbia (Australia)": 147, "Columbia (Baltica)": 156,
                            "Columbia (East Antarctica)": 159, "Columbia (Greenland)": 157,
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
                            "Eurasia (W Siberia)": 69, "Eurasia (W Siberia & Central Asia)": 68,
                            "Europe": 71, "Europe (Cis-Caspian)": 72, "Gondwana (Africa)": 73,
                            "Gondwana (Antarctica)": 74, "Gondwana (Arabia)": 126, "Gondwana (Armorica)": 75,
                            "Gondwana (Australia)": 76, "Gondwana (Indostan)": 77, "Gondwana (N Africa)": 78,
                            "Gondwana (N Africa [Tethys palaeocean])": 79, "Gondwana (New Caledonia)": 131,
                            "Gondwana (New Zealand)": 132, "Gondwana (Perunica)": 80, "Gondwana (S America)": 81,
                            "Gondwana (Sardinia)": 113, "Gondwana (Saxo-Thuringia)": 82,
                            "Gondwana (South Africa)": 124, "Gondwana (South America)": 83,
                            "Kazakhstania": 84, "Kazakhstania (Xinjiang)": 85, "Kenorland (Baltica)": 168,
                            "Kenorland (Kalaharia)": 169, "Kenorland (Laurentia)": 167,
                            "Kenorland (Western Australia)": 170, "Kitakamiland": 86, "Laurentia": 87,
                            "Laurussia": 88, "Laurussia (Anatolia)": 89, "Laurussia (Armorica)": 90,
                            "Laurussia (Avalonia)": 93, "Laurussia (Avalonia & Baltica)": 92,
                            "Laurussia (Baltica)": 94, "Laurussia (Cantabria)": 95, "Laurussia (Iberica)": 96,
                            "Laurussia (Laurentia)": 97, "Laurussia (Moesia)": 98, "Laurussia (Moldanubia)": 125,
                            "Laurussia (Perunica)": 90, "Laurussia (Rhenano-Hercynia)": 100,
                            "Laurussia (Saxo-Thuringia)": 101, "Moldanubia": 102, "Mongolia (Western)": 103,
                            "not specified": 106, "Pacific": 107, "Pamir-Alaj": 108, "Pannotia (Antarctica)": 174,
                            "Pannotia (Indostan)": 175, "Pannotia (Siberia)": 150, "Perunica": 109,
                            "Proangarida": 110, "Rodinia": 111, "Rodinia (Amazonia)": 141,
                            "Rodinia (Australia)": 146, "Rodinia (Baltica)": 148, "Rodinia (Indostan)": 138,
                            "Rodinia (Laurentia)": 140, "Rodinia (North China)": 112, "Rodinia (Rio Plato)": 142,
                            "Rodinia (Siberia)": 149, "Rodinia (South China)": 139, "Siberia": 114,
                            "Sibumasu": 115, "Superior Craton (Superior Craton)": 171,
                            "Tibet": 116, "Tien Shan": 117, "Tien Shan (North)": 118, "Tien Shan (South)": 133,
                            "Tuva": 119, "unknown": 120, "Vaalbara (Kaapvaal)": 165, "Vaalbara (Pilbara)": 166,
                            "Xinjiang": 121
                            }
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183"}
        self.result = []
        self.df = None

    def set_form(self, name, first_symbols=False, order=None, orderDirection=None, author=None, original_spelling=None,
                 yearFrom=None, yearTo=None, rank_list=None, paleoregion_list=None, journal=None, abbreviation=None):
        """
        :param name: request; str
        :param first_symbols: optional; bool
        :param order: optional; one of ["name", "yearFrom", "title", "titleOrig", "titleAbbr", "lastName"]
        :param orderDirection: optional; one of ["desc", "asc"]
        :param author: optional; str
        :param original_spelling: optional; str
        :param yearFrom: optional; int or str
        :param yearTo: optional; int or str
        :param rank_list: optional; list
        :param paleoregion_list: optional; list
        :param journal: optional; str
        :param abbreviation: optional; str
        :return: nothing
        """
        self.form["Name"] = name
        if first_symbols and isinstance(first_symbols, bool):
            self.form["searchOnlyByFirstSymbols"] = "on"
        if order and orderDirection and isinstance(order, str) and isinstance(orderDirection, str):
            self.form["sort by"]["order"] = order
            self.form["sort by"]["orderDirection"] = orderDirection
        if author and isinstance(author, str):
            self.form["extended search"]["author"] = author
        if original_spelling and isinstance(original_spelling, str):
            self.form["extended search"]["original spelling"] = original_spelling
        if yearFrom and (isinstance(yearFrom, str) or isinstance(yearFrom, int)):
            self.form["extended search"]["yearFrom"] = str(yearFrom)
        if yearTo and (isinstance(yearTo, str) or isinstance(yearTo, int)):
            self.form["extended search"]["yearTo"] = str(yearTo)
        if rank_list and isinstance(rank_list, list):
            self.form["extended search"]["rank"] = rank_list
        if paleoregion_list and isinstance(paleoregion_list, list):
            self.form["extended search"]["paleoregion"] = paleoregion_list
        if journal and isinstance(journal, str):
            self.form["extended search"]["journal"] = journal
        if abbreviation and isinstance(abbreviation, str):
            self.form["extended search"]["abbreviation"] = abbreviation

    def merge_url(self):
        url = ''.join([self.url_base, self.lists, self.url_end])
        tem_list = [url]
        if self.lists == "name":
            return url
        elif self.lists in ["supragenus", "genus", "infragenus", "species", "infraspecies"]:
            tem_list.append("name=%s" % self.form["Name"])
            tem_list.append("searchOnlyByFirstSymbols=%s" % self.form["searchOnlyByFirstSymbols"])
            tem_list.append("order=%s" % self.form["sort by"]["order"])
            tem_list.append("orderDirection=%s" % self.form["sort by"]["orderDirection"])
            tem_list.append("author=%s" % self.form["extended search"]["author"])
            tem_list.append("titleOrig=%s" % self.form["extended search"]["original spelling"])
            tem_list.append("yearFrom=%s" % self.form["extended search"]["yearFrom"])
            tem_list.append("yearTo=%s" % self.form["extended search"]["yearTo"])
            if self.lists == "supragenus":
                for rank in self.form["extended search"]["rank"]:
                    tem_list.append("rankID[]=%i" % self.rank_supragenus[rank])
                return '&'.join(tem_list)

            elif self.lists == "genus":
                for rank in self.form["extended search"]["rank"]:
                    tem_list.append("rankID[]=%i" % self.rank_genus[rank])
                return '&'.join(tem_list)
            elif self.lists == "infragenus":
                for rank in self.form["extended search"]["rank"]:
                    tem_list.append("rankID[]=%i" % self.rank_infragenus[rank])
                return '&'.join(tem_list)
            elif self.lists == "species":
                for rank in self.form["extended search"]["rank"]:
                    tem_list.append("rankID[]=%i" % self.rank_species[rank])
                for pr in self.form["extended search"]["paleoregion"]:
                    tem_list.append("paleoID=%i" % self.paleoregion[pr])
                return '&'.join(tem_list)
            else:
                for rank in self.form["extended search"]["rank"]:
                    tem_list.append("rankID[]=%i" % self.rank_infraspecies[rank])
                for pr in self.form["extended search"]["paleoregion"]:
                    tem_list.append("paleoID=%i" % self.paleoregion[pr])
                return '&'.join(tem_list)

        elif self.lists in ["publication", "book", "journal"]:
            tem_list.append("title=%s" % self.form["Name"])
            tem_list.append("searchOnlyByFirstSymbols=%s" % self.form["searchOnlyByFirstSymbols"])
            tem_list.append("order=%s" % self.form["sort by"]["order"])
            tem_list.append("orderDirection=%s" % self.form["sort by"]["orderDirection"])
            if self.lists == "publication":
                tem_list.append("author=%s" % self.form["extended search"]["author"])
                tem_list.append("titleOrig=%s" % self.form["extended search"]["original spelling"])
                tem_list.append("yearFrom=%s" % self.form["extended search"]["yearFrom"])
                tem_list.append("yearTo=%s" % self.form["extended search"]["yearTo"])
                tem_list.append("journalID=%s" % self.form["extended search"]["journal"])
                return '&'.join(tem_list)
            elif self.lists == "book":
                tem_list.append("titleOrig=%s" % self.form["extended search"]["original spelling"])
                tem_list.append("titleAbbr=%s" % self.form["extended search"]["abbreviation"])
                return '&'.join(tem_list)
            else:
                tem_list.append("titleOrig=%s" % self.form["extended search"]["original spelling"])
                tem_list.append("yearFrom=%s" % self.form["extended search"]["yearFrom"])
                tem_list.append("yearTo=%s" % self.form["extended search"]["yearTo"])
                return '&'.join(tem_list)
        else:
            tem_list.append("lastName=%s" % self.form["Name"])
            tem_list.append("searchOnlyByFirstSymbols=%s" % self.form["searchOnlyByFirstSymbols"])
            tem_list.append("order=%s" % self.form["sort by"]["order"])
            tem_list.append("orderDirection=%s" % self.form["sort by"]["orderDirection"])
            return '&'.join(tem_list)

    def execute_URL(self, lists, name, first_symbols=False, order=None, orderDirection=None, author=None,
                    original_spelling=None, yearFrom=None, yearTo=None, rank_list=None, paleoregion_list=None,
                    journal=None, abbreviation=None):
        """
        :param lists:
        :param name:
        :param first_symbols:
        :param order:
        :param orderDirection:
        :param author:
        :param original_spelling:
        :param yearFrom:
        :param yearTo:
        :param rank_list:
        :param paleoregion_list:
        :param journal:
        :param abbreviation:
        :return:
        """
        if isinstance(lists, str):
            self.lists = lists
        self.set_form(name, first_symbols, order, orderDirection, author, original_spelling, yearFrom, yearTo,
                      rank_list, paleoregion_list, journal, abbreviation)
        return self.merge_url()

    def supragenus(self, name, first_symbols=False, order=None, orderDirection=None, author=None,
                   original_spelling=None, yearFrom=None, yearTo=None, rank_list=None, save_to_csv=None):
        """
        :param save_to_csv:
        :param name: necessary, str
        :param first_symbols: optional, bool[False]
        :param order: optional, str[name, yearFrom]
        :param orderDirection: optional, str[desc, asc]
        :param author: optional, str
        :param original_spelling: optional, str
        :param yearFrom: optional, str/int
        :param yearTo: optional, str/int
        :param rank_list: optional, list
        :return: url, str
        """
        url = self.execute_URL(lists="supragenus", name=name, first_symbols=first_symbols, order=order,
                               orderDirection=orderDirection,
                               author=author, original_spelling=original_spelling, yearFrom=yearFrom, yearTo=yearTo,
                               rank_list=rank_list)
        self.execute(url, name, save_to_csv)

    def execute(self, url, name, save_to_csv):
        self.result.clear()
        res = self.requests3(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        total_count_num = soup.find("div", class_="list-group").find("h4").text.split(' ')[-1]
        total_page_num = math.ceil(int(total_count_num) / 10)
        print(f"{name}: There is/are {total_count_num} results found by {self.lists} search in {total_page_num} pages.")
        for page in range(1, total_page_num + 1):
            tem_url = "&".join([url, "page=%i" % page])
            tem_res = self.requests3(tem_url)
            tem_soup = BeautifulSoup(tem_res.text, "html.parser")
            list_group_item = tem_soup.find("div", class_="list-group").find_all("span", class_="list-group-item")
            items = tqdm(list_group_item)
            for item in items:
                items.set_description(f"    |______ executing page {page}: {len(list_group_item)} items.")
                tem_item = {}
                try:
                    tem_item["href"] = self.url_base + item.find("h1").find("a")["href"]
                except:
                    pass
                info_res = self.requests3(tem_item["href"])
                info_soup = BeautifulSoup(info_res.text, 'html.parser')
                tem_item["IDNAME"] = info_soup.find('div', class_="panel-heading").find_all("span")[-1].text
                dl = info_soup.find("dl", class_="dl-horizontal")
                for i in dl.find_all("dt"):
                    column_label = i.text.strip()
                    column_value = i.find_next("dd")
                    try:
                        tem_item[column_label] = column_value.text.strip()
                        tem_item[column_label + ' href'] = self.url_base + column_value.find('a')['href']
                    except:
                        tem_item[column_label] = column_value.text.strip()

                self.result.append(tem_item)
        for i in self.result:
            self.df = pd.concat([self.df, pd.DataFrame.from_dict(i, orient="index").T], ignore_index=True)
        if save_to_csv:
            if save_to_csv.endswith(".csv"):
                self.df.to_csv(save_to_csv)
            else:
                self.df.to_csv(f"{save_to_csv}.csv")
        else:
            self.df.to_csv(f"{name}.csv")

    def genus(self, name, first_symbols=False, order=None, orderDirection=None, author=None, original_spelling=None,
              yearFrom=None, yearTo=None, rank_list=None, save_to_csv=None):
        url = self.execute_URL(lists="genus", name=name, first_symbols=first_symbols, order=order,
                               orderDirection=orderDirection,
                               author=author, original_spelling=original_spelling, yearFrom=yearFrom, yearTo=yearTo,
                               rank_list=rank_list)
        self.execute(url, name, save_to_csv)

    def infragenus(self, name, first_symbols=False, order=None, orderDirection=None, author=None,
                   original_spelling=None,
                   yearFrom=None, yearTo=None, rank_list=None, save_to_csv=None):
        url = self.execute_URL(lists="infragenus", name=name, first_symbols=first_symbols, order=order,
                               orderDirection=orderDirection,
                               author=author, original_spelling=original_spelling, yearFrom=yearFrom, yearTo=yearTo,
                               rank_list=rank_list)
        self.execute(url, name, save_to_csv)

    def species(self, name, first_symbols=False, order=None, orderDirection=None, author=None, original_spelling=None,
                yearFrom=None, yearTo=None, rank_list=None, paleoregion_list=None, save_to_csv=None):
        url = self.execute_URL(lists="species", name=name, first_symbols=first_symbols, order=order,
                               orderDirection=orderDirection,
                               author=author, original_spelling=original_spelling, yearFrom=yearFrom, yearTo=yearTo,
                               rank_list=rank_list,
                               paleoregion_list=paleoregion_list)
        self.execute(url, name, save_to_csv)

    def infraspecies(self, name, first_symbols=False, order=None, orderDirection=None, author=None,
                     original_spelling=None,
                     yearFrom=None, yearTo=None, rank_list=None, paleoregion_list=None, save_to_csv=None):
        url = self.execute_URL(lists="infraspecies", name=name, first_symbols=first_symbols, order=order,
                               orderDirection=orderDirection,
                               author=author, original_spelling=original_spelling, yearFrom=yearFrom, yearTo=yearTo,
                               rank_list=rank_list,
                               paleoregion_list=paleoregion_list)
        self.execute(url, name, save_to_csv)

    def publication(self, title, first_symbols=False, order=None, orderDirection=None, author=None,
                    original_spelling=None,
                    yearFrom=None, yearTo=None, journal=None, save_to_csv=None):
        url = self.execute_URL(lists="publication", name=title, first_symbols=first_symbols, order=order,
                               orderDirection=orderDirection, author=author, original_spelling=original_spelling,
                               yearFrom=yearFrom, yearTo=yearTo, journal=journal)
        self.execute(url, title, save_to_csv)

    def book(self, title, first_symbols=False, order=None, orderDirection=None, original_spelling=None,
             abbreviation=None, save_to_csv=None):
        url = self.execute_URL(lists="book", name=title, first_symbols=first_symbols, order=order,
                               orderDirection=orderDirection, original_spelling=original_spelling,
                               abbreviation=abbreviation)
        self.execute(url, title, save_to_csv)

    def journal(self, title, first_symbols=False, order=None, orderDirection=None, original_spelling=None,
                yearFrom=None, yearTo=None, save_to_csv=None):
        url = self.execute_URL(lists="journal", name=title, first_symbols=first_symbols, order=order,
                               orderDirection=orderDirection, original_spelling=original_spelling,
                               yearFrom=yearFrom, yearTo=yearTo)
        self.execute(url, title, save_to_csv)

    def author(self, lastName, first_symbols=False, order=None, orderDirection=None, save_to_csv=None):
        url = self.execute_URL(lists="author", name=lastName, first_symbols=first_symbols, order=order,
                               orderDirection=orderDirection)
        self.execute(url, lastName, save_to_csv)

    def requests3(self, url):
        for i in range(3):
            try:
                res = requests.get(url, headers=self.headers)
                return res
            except:
                time.sleep(5)


if __name__ == "__main__":
    pyifpni = pyIFPNI()
    # pyifpni.supragenus("Orchidaceae", save_to_csv="orchiaceae")
    # pyifpni.genus("mahonia")
    # pyifpni.species("achlys")
    pyifpni.species("mahonia", save_to_csv="mahonia speices")
