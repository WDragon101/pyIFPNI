<!-- TOC -->
* [Background](#background)
* [Introduction](#introduction)
* [Install pyIFPNI package](#install-pyifpni-package)
* [Start](#start)
* [Basic functions based on taxonomic hierarchy](#basic-functions-based-on-taxonomic-hierarchy)
  * [1. supragenus()](#1-supragenus--)
    * [1.1. parameters of supragenus()](#11-parameters-of-supragenus--)
    * [1.2. supragenus function example](#12-supragenus-function-example)
  * [2. genus()](#2-genus--)
    * [2.1. parameters of genus()](#21-parameters-of-genus--)
    * [2.2. genus() function example](#22-genus---function-example)
  * [3. infragenus()](#3-infragenus--)
    * [3.1. parameters of infragenus()](#31-parameters-of-infragenus--)
    * [3.2. infragenus() function example](#32-infragenus---function-example)
  * [4. species()](#4-species--)
    * [4.1. parameters of species()](#41-parameters-of-species--)
    * [4.2. species() function example](#42-species---function-example)
  * [5. infraspecies()](#5-infraspecies--)
    * [5.1. parameters of infraspecies()](#51-parameters-of-infraspecies--)
    * [5.2. infraspecies() function example](#52-infraspecies---function-example)
* [Basic functions based on bibliography](#basic-functions-based-on-bibliography)
  * [6. publication()](#6-publication--)
    * [6.1. parameters of publication()](#61-parameters-of-publication--)
    * [6.2. publication() function example](#62-publication---function-example)
  * [7. book()](#7-book--)
    * [7.1. parameters of book()](#71-parameters-of-book--)
    * [7.2. book() function example](#72-book---function-example)
  * [8. journal()](#8-journal--)
    * [8.1. parameters of journal()](#81-parameters-of-journal--)
    * [8.2. journal() function example](#82-journal---function-example)
  * [9. Paleobotanists query method: author()](#9-paleobotanists-query-method--author--)
    * [9.1. parameters of author()](#91-parameters-of-author--)
    * [9.2. author() function example](#92-author---function-example)
* [Advanced functions](#advanced-functions)
  * [10. supragenus_ancestors()](#10-supragenus_ancestors--)
    * [10.1. parameters of supragenus_ancestors()](#101-parameters-of-supragenus_ancestors--)
    * [10.2. supragenus_ancestors function example](#102-supragenus_ancestors-function-example)
  * [11. genus_ancestors()](#11-genus_ancestors--)
    * [11.1. parameters of genus_ancestors()](#111-parameters-of-genus_ancestors--)
    * [11.2. genus_ancestors function example](#112-genus_ancestors-function-example)
  * [12. infragenus_ancestors()](#12-infragenus_ancestors--)
    * [12.1. parameters of infragenus_ancestors()](#121-parameters-of-infragenus_ancestors--)
    * [12.2. infragenus_ancestors function example](#122-infragenus_ancestors-function-example)
  * [13. species_ancestors()](#13-species_ancestors--)
    * [13.1. parameters of species_ancestors()](#131-parameters-of-species_ancestors--)
    * [13.2. species_ancestors function example](#132-species_ancestors-function-example)
  * [14. infraspecies_ancestors()](#14-infraspecies_ancestors--)
    * [14.1. parameters of infraspecies_ancestors()](#141-parameters-of-infraspecies_ancestors--)
    * [14.2. infraspecies_ancestors function example](#142-infraspecies_ancestors-function-example)
  * [15. supragenus_descendants()](#15-supragenus_descendants--)
    * [15.1. parameters of supragenus_descendants()](#151-parameters-of-supragenus_descendants--)
    * [15.2. supragenus_descendants function example](#152-supragenus_descendants-function-example)
  * [16. genus_descendants()](#16-genus_descendants--)
    * [16.1. parameters of genus_descendants()](#161-parameters-of-genus_descendants--)
    * [16.2. genus_descendants function example](#162-genus_descendants-function-example)
  * [17. infragenus_descendants()](#17-infragenus_descendants--)
    * [17.1. parameters of infragenus_descendants()](#171-parameters-of-infragenus_descendants--)
    * [17.2. infragenus_descendants function example](#172-infragenus_descendants-function-example)
  * [18. species_descendants()](#18-species_descendants--)
    * [18.1. parameters of species_descendants()](#181-parameters-of-species_descendants--)
    * [18.2. species_descendants function example](#182-species_descendants-function-example)
  * [19. infraspecies_descendants()](#19-infraspecies_descendants--)
    * [19.1. parameters of infraspecies_descendants()](#191-parameters-of-infraspecies_descendants--)
    * [19.2. infraspecies_descendants function example](#192-infraspecies_descendants-function-example)
  * [20. publication2taxon()](#20-publication2taxon--)
    * [20.1. parameters of publication2taxon()](#201-parameters-of-publication2taxon--)
    * [20.2. publication2taxon function example](#202-publication2taxon-function-example)
  * [21. book2taxon()](#21-book2taxon--)
    * [21.1. parameters of book2taxon()](#211-parameters-of-book2taxon--)
    * [21.2. book2taxon function example](#212-book2taxon-function-example)
  * [22. journal2taxon()](#22-journal2taxon--)
    * [22.1. parameters of journal2taxon()](#221-parameters-of-journal2taxon--)
    * [22.2. journal2taxon function example](#222-journal2taxon-function-example)
  * [23. author2publication()](#23-author2publication--)
    * [23.1. parameters of author2publication()](#231-parameters-of-author2publication--)
    * [23.2. author2publication() function example](#232-author2publication---function-example)
  * [24. author2taxon()](#24-author2taxon--)
    * [24.1. parameters of author2taxon()](#241-parameters-of-author2taxon--)
    * [24.2. author2taxon() function example](#242-author2taxon---function-example)
* [Other information](#other-information)
  * [Available rank hierarchy lists for different functions](#available-rank-hierarchy-lists-for-different-functions)
    * [rank of supragenus](#rank-of-supragenus)
    * [rank of genus](#rank-of-genus)
    * [rank of infragenus](#rank-of-infragenus)
    * [rank of species](#rank-of-species)
    * [rank of infraspecies](#rank-of-infraspecies)
  * [Available paleoregion list for species() and infraspecies()](#available-paleoregion-list-for-species---and-infraspecies--)
<!-- TOC -->

# Background

This is a python package accessing to IFPNI flexible. It supplies several functions according to different rank, such as *supragenus*, *genus*, *infragenus*, *species*, *infraspecies*.

In current version, moreover, it also supplies some advanced functions that can search items from *supragenus* to *infraspecies* by hierarchy or reverse.
# Introduction
Here, I will introduce all functions and give examples to show you how to use them.


# Install pyIFPNI package

> pip install pyIFPNI

# Start
After installed pyIFPNI, it is suggested that you initiated this package with following codes:
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()
```

# Basic functions based on taxonomic hierarchy
Researchers have the flexibility to employ different query methods while accessing fossil plant name records. These methods enable them to efficiently navigate through the records by utilizing various classification levels.
## 1. supragenus()
The supragenus() function enables researchers to query fossilized plant name records at taxonomic ranks higher than the genus level.
### 1.1. parameters of supragenus()
This function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to this function, you can view the list of available ranks in **Other information**.

### 1.2. supragenus function example
**Example**: *supragenus* querying *orchidaceae*

This is a simple example to show you how to use *supragenus*.

When you run the following code, *supragenus* function will retrieve all items relate to *orchidaceae*
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

orchi = ifpni.supragenus(name='orchidaceae')

print(orchi)

# save result to csv file
orchi.to_csv("./suprageus_orchidaceae.csv")
```

You can watch the retrieval process in the console:
```
--------------------Proceeding  supragenus  (based on taxonomic) method--------------------
Searching about: orchidaceae
There is/are 2 result(s) founded on 1 page(s).
	|______ executing page 1: 2 items.: 100%|██████████| 2/2 [00:12<00:00,  6.13s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

This package will not save data automatically, so you can manually save result to CSV file. If you are familiar with pandas.dataframe, it will be easy to save the data to a file.

Here, I recommend pandas.dataframe.to_csv().
```python
# view the result
print(orchi)

# save result to csv file
orchi.to_csv("./suprageus_orchidaceae.csv")
```

You will see the results in the console, as well as the saved **supragenus_orchidaceae.csv** file in current folder.
```
                                                href  ...                                          Type href
0  http://ifpni.org//supragenus.htm?id=992C341F-8...  ...                                                NaN
1  http://ifpni.org//supragenus.htm?id=0604FB97-B...  ...  http://ifpni.org//genus.htm?id=C2D639DB-1CD0-4...

[2 rows x 26 columns]
```

## 2. genus()
The genus() function assists in querying fossilized plant name records at the genus level.
### 2.1. parameters of genus()
This function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to this function, you can view the list of available ranks in **Other information**.
### 2.2. genus() function example
**Example**: *genus* querying *achlys*
Just like how to use *supragenus*, this example will retrieve any item relate  to *achlys* in genus level.
And we want to save the result to *genus_achlys.csv* file in current folder.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

ach = ifpni.genus(name='achlys')

print(ach)

# save result to csv file
ach.to_csv("./genus_achlys.csv")
```
In the console:
```base
--------------------Proceeding  genus  (based on taxonomic) method--------------------
Searching about: achlys
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:02<00:00,  2.12s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ...                                  Parent Taxon href
0  http://ifpni.org//genus.htm?id=D30DF6EC-972F-D...  ...  http://ifpni.org//supragenus.htm?id=F14DD416-D...

[1 rows x 11 columns]
```
## 3. infragenus()
To further refine the search below the genus level, the infragenus() function comes into play.
### 3.1. parameters of infragenus()
This function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to this function, you can view the list of available ranks in **Other information**.
### 3.2. infragenus() function example
**Example**: *infragenus* querying *Sphenopteris*
This is a simple way to utilize *infragenus* function. The following codes will return items relate to *Sphenopteris* and save them to *infragenus_sphenopteris.csv* file.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

sph = ifpni.infragenus(name="Sphenopteris")

print(sph)

# save result to csv file
sph.to_csv("./infragenus_sphenopteris.csv")
```
In the console:
```base
--------------------Proceeding  infragenus  (based on taxonomic) method--------------------
Searching about: Sphenopteris
There is/are 16 result(s) founded on 2 page(s).
	|______ executing page 1: 10 items.: 100%|██████████| 10/10 [02:49<00:00, 16.97s/it]
	|______ executing page 2: 6 items.: 100%|██████████| 6/6 [02:19<00:00, 23.17s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                 href  ...                                Authors (Name) href
0   http://ifpni.org//infragenus.htm?id=2CCDF6FC-A...  ...                                                NaN
1   http://ifpni.org//infragenus.htm?id=954D40CD-0...  ...                                                NaN
2   http://ifpni.org//infragenus.htm?id=CD40E831-3...  ...                                                NaN
3   http://ifpni.org//infragenus.htm?id=9AF725A8-2...  ...                                                NaN
4   http://ifpni.org//infragenus.htm?id=E91515E6-E...  ...                                                NaN
5   http://ifpni.org//infragenus.htm?id=D1550C9D-6...  ...                                                NaN
6   http://ifpni.org//infragenus.htm?id=03791082-F...  ...                                                NaN
7   http://ifpni.org//infragenus.htm?id=C0A79D94-9...  ...                                                NaN
8   http://ifpni.org//infragenus.htm?id=02F1408A-9...  ...                                                NaN
9   http://ifpni.org//infragenus.htm?id=3A9AFFA0-2...  ...                                                NaN
10  http://ifpni.org//infragenus.htm?id=E607B6DA-7...  ...                                                NaN
11  http://ifpni.org//infragenus.htm?id=0D2D05B4-9...  ...                                                NaN
12  http://ifpni.org//infragenus.htm?id=0BF2A6C3-9...  ...  http://ifpni.org//author.htm?id=C0DDE698-5FAB-...
13  http://ifpni.org//infragenus.htm?id=FF15818A-1...  ...                                                NaN
14  http://ifpni.org//infragenus.htm?id=94D0D060-3...  ...  http://ifpni.org//author.htm?id=B66B4C7F-E3CD-...
15  http://ifpni.org//infragenus.htm?id=851AC57F-9...  ...                                                NaN

[16 rows x 34 columns]
```
## 4. species()
When researchers focus on the most fundamental taxonomic rank, the species() function becomes relevant. They can utilize this method to query fossilized plant name records specifically associated with particular species or genera.
### 4.1. parameters of species()
This function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to this function, you can view the list of available ranks in **Other information**.
- *paleoregion_list*: (Default:None) choose the paleoregions available to this function, you can view the list of available paleoregions in **Other information**.
### 4.2. species() function example
**Example**: *species* querying *Cordaites*
Generally speaking, this function will cost more time than *supragenus*, *genus*, *infragenus* and *infraspecies*.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

cor = ifpni.species(name="Cordaites")

print(cor)

# save result to csv file
cor.to_csv("./species_cordaites.csv")
```
In the console:
```base
--------------------Proceeding  species  (based on taxonomic) method--------------------
Searching about: Cordaites
There is/are 79 result(s) founded on 8 page(s).
	|______ executing page 1: 10 items.: 100%|██████████| 10/10 [00:50<00:00,  5.04s/it]
	|______ executing page 2: 10 items.: 100%|██████████| 10/10 [00:47<00:00,  4.74s/it]
	|______ executing page 3: 10 items.: 100%|██████████| 10/10 [00:36<00:00,  3.64s/it]
	|______ executing page 4: 10 items.: 100%|██████████| 10/10 [00:29<00:00,  2.92s/it]
	|______ executing page 5: 10 items.: 100%|██████████| 10/10 [00:34<00:00,  3.50s/it]
	|______ executing page 6: 10 items.: 100%|██████████| 10/10 [01:02<00:00,  6.27s/it]
	|______ executing page 7: 10 items.: 100%|██████████| 10/10 [00:58<00:00,  5.80s/it]
	|______ executing page 8: 9 items.: 100%|██████████| 9/9 [00:30<00:00,  3.43s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                 href  ... Edition
0   http://ifpni.org//species.htm?id=3C6A4B88-0B69...  ...     NaN
1   http://ifpni.org//species.htm?id=76D9A721-6D7F...  ...     NaN
2   http://ifpni.org//species.htm?id=A20A1B75-5E3C...  ...     NaN
3   http://ifpni.org//species.htm?id=EA5621CD-3EF1...  ...     NaN
4   http://ifpni.org//species.htm?id=A57C3B40-6ECB...  ...     NaN
..                                                ...  ...     ...
74  http://ifpni.org//species.htm?id=F971EB97-DF0B...  ...     NaN
75  http://ifpni.org//species.htm?id=539290B4-6ABF...  ...     NaN
76  http://ifpni.org//species.htm?id=22D7A7C7-0535...  ...     NaN
77  http://ifpni.org//species.htm?id=20100452-E5E2...  ...     NaN
78  http://ifpni.org//species.htm?id=D6B63F53-F2C2...  ...     NaN

[79 rows x 45 columns]
```
## 5. infraspecies()
The infraspecies() function allows researchers to delve even deeper into the taxonomic hierarchy, exploring fossilized plant name records below the species level. This method is particularly useful for investigating subspecies, varieties, or forms of fossilized plants.
### 5.1. parameters of infraspecies()
This function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to this function, you can view the list of available ranks in **Other information**.
- *paleoregion_list*: (Default:None) choose the paleoregions available to this function, you can view the list of available paleoregions in **Other information**.
### 5.2. infraspecies() function example
**Example**: *infraspecies* querying *Lophozonotriletes*
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

lop = ifpni.infraspecies(name="Lophozonotriletes")

print(lop)

# save result to csv file
lop.to_csv("./infraspecies_Lophozonotriletes.csv")
```
In the console:
```base
--------------------Proceeding  infraspecies  (based on taxonomic) method--------------------
Searching about: Lophozonotriletes
There is/are 3 result(s) founded on 1 page(s).
	|______ executing page 1: 3 items.: 100%|██████████| 3/3 [00:07<00:00,  2.60s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ... Issue
0  http://ifpni.org//infraspecies.htm?id=4C8BDA17...  ...   NaN
1  http://ifpni.org//infraspecies.htm?id=0D048267...  ...   NaN
2  http://ifpni.org//infraspecies.htm?id=BEF94CA3...  ...     3

[3 rows x 30 columns]
```
# Basic functions based on bibliography
These methods allow users to retrieve references based on the type of publication they belong to.
## 6. publication()
This method retrieves all types of publications, including books, journal articles, conference proceedings, reports, theses, etc. When using the publication() method, you generally get a broader range of results encompassing various publication types.
### 6.1. parameters of publication()
This function contains several parameters as below:
- *title*: (Required) the name of publication that you interested.
- *first_symbols*:  (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["title","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *journal*: (Default: None) only return items published by given journal.
### 6.2. publication() function example
**Example**: *publication* querying *"Proposal to conserve the name"*
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

p = ifpni.publication(title="Proposal to conserve the name")

print(p)

# save result to csv file
p.to_csv("./publication_Proposal_to_conserve_the_name.csv")
```
In the console:
```base
--------------------Proceeding  publication  (based on publication) method--------------------
Searching about: Proposal to conserve the name
There is/are 66 result(s) founded on 7 page(s).
	|______ executing page 1: 10 items.: 100%|██████████| 10/10 [01:27<00:00,  8.76s/it]
	|______ executing page 2: 10 items.: 100%|██████████| 10/10 [03:01<00:00, 18.19s/it]
	|______ executing page 3: 10 items.: 100%|██████████| 10/10 [02:45<00:00, 16.58s/it]
	|______ executing page 4: 10 items.: 100%|██████████| 10/10 [02:56<00:00, 17.65s/it]
	|______ executing page 5: 10 items.: 100%|██████████| 10/10 [03:01<00:00, 18.14s/it]
	|______ executing page 6: 10 items.: 100%|██████████| 10/10 [03:00<00:00, 18.04s/it]
	|______ executing page 7: 6 items.: 100%|██████████| 6/6 [00:22<00:00,  3.75s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                 href  ...                                           DOI href
0   http://ifpni.org//publication.htm?id=44CE2B21-...  ...  http://ifpni.org/http://dx.doi.org/10.2307/122...
1   http://ifpni.org//publication.htm?id=328B8AB1-...  ...  http://ifpni.org/http://dx.doi.org/10.2307/155...
2   http://ifpni.org//publication.htm?id=655D2348-...  ...  http://ifpni.org/http://dx.doi.org/10.1002/tax...
3   http://ifpni.org//publication.htm?id=EA45F8D7-...  ...  http://ifpni.org/http://dx.doi.org/10.1002/tax...
4   http://ifpni.org//publication.htm?id=4CF211A2-...  ...  http://ifpni.org/http://dx.doi.org/10.1002/tax...
..                                                ...  ...                                                ...
61  http://ifpni.org//publication.htm?id=EC03F228-...  ...  http://ifpni.org/http://dx.doi.org/10.1002/tax...
62  http://ifpni.org//publication.htm?id=8BCDC7F6-...  ...  http://ifpni.org/http://dx.doi.org/10.1002/tax...
63  http://ifpni.org//publication.htm?id=CB84580C-...  ...  http://ifpni.org/http://dx.doi.org/10.1002/tax...
64  http://ifpni.org//publication.htm?id=9605A02A-...  ...                                                NaN
65  http://ifpni.org//publication.htm?id=A9A5592C-...  ...  http://ifpni.org/http://dx.doi.org/10.12705/64...

[66 rows x 16 columns]
```
## 7. book()
This method specifically retrieves references that belong to books. It is useful when searching for information contained within published books. Using the book() method helps narrow down your search to relevant book titles and their associated details such as author(s), title, publisher, year, etc.
### 7.1. parameters of book()
This function contains several parameters as below:
- *title*: (Required) the name of publication that you interested.
- *first_symbols*:  (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["title","titleOrigin","titleAbbr"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *abbreviation*: (Default:None) only return items that has the given abbreviation.
### 7.2. book() function example
**Example**: *book* querying *"Beiträge zur Kenntniss der fossilen Flora"*
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

b = ifpni.book(title="Beiträge zur Kenntniss der fossilen Flora")

print(b)

# save result to csv file
b.to_csv("./book_Beiträge_zur_Kenntniss_der_fossilen_Flora.csv")
```
In the console:
```base
--------------------Proceeding  book  (based on publication) method--------------------
Searching about: Beiträge zur Kenntniss der fossilen Flora
There is/are 5 result(s) founded on 1 page(s).
	|______ executing page 1: 5 items.: 100%|██████████| 5/5 [01:16<00:00, 15.28s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ...    TL2
0  http://ifpni.org//book.htm?id=B72F4D7B-6C75-65...  ...    NaN
1  http://ifpni.org//book.htm?id=5FFACAD9-880B-74...  ...    NaN
2  http://ifpni.org//book.htm?id=024A137C-A481-47...  ...  33442
3  http://ifpni.org//book.htm?id=2F447F69-A31F-40...  ...  33437
4  http://ifpni.org//book.htm?id=C97F6B9C-A50C-40...  ...  33437

[5 rows x 9 columns]
```
## 8. journal()
This method focuses on retrieving references from academic journals. If you are specifically interested in scholarly articles published in journals, using the journal() method can help filter out other types of publications.
### 8.1. parameters of journal()
This function contains several parameters as below:
- *title*: (Required) the name of publication that you interested.
- *first_symbols*:  (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["title","titleOrigin"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
### 8.2. journal() function example
**Example**: *journal* querying *"Acta Palaeontologica"*
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

j = ifpni.journal(title="Acta Palaeontologica")

print(j)

# save result to csv file
j.to_csv("./journal_Acta_Palaeontologica.csv")
```
In the console:
```base
--------------------Proceeding  journal  (based on publication) method--------------------
Searching about: Acta Palaeontologica
There is/are 3 result(s) founded on 1 page(s).
	|______ executing page 1: 3 items.: 100%|██████████| 3/3 [00:13<00:00,  4.49s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ...                Original spelling
0  http://ifpni.org//journal.htm?id=11CCBF51-F3D7...  ...                              NaN
1  http://ifpni.org//journal.htm?id=6357910E-D63C...  ...                              NaN
2  http://ifpni.org//journal.htm?id=CAA4E567-7654...  ...  古生物学报 [Gushengwu xuebao: jikan]

[3 rows x 8 columns]
```
## 9. Paleobotanists query method: author()
Within the pyIFPNI library, there is a specialized method called author() that empowers users to explore paleobotanists listed in the IFPNI database. This dedicated functionality facilitates convenient access to information regarding specific authors who have made significant contributions to the field of paleobotany, with their work thoroughly documented in the IFPNI repository. By making use of the author() method, researchers can efficiently retrieve relevant data related to these paleobotanists and gain valuable insights into their notable contributions
### 9.1. parameters of author()
This function contains several parameters as below:
- *lastName*: (Required) the name of paleobotanist that you interested.
- *first_symbols*:  (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["lastName"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
### 9.2. author() function example
**Example**: *author* querying *"Acta Palaeontologica"*
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

abr = ifpni.author(lastName="Abramova")

print(abr)

# save result to csv file
abr.to_csv("./author_Abramova.csv")
```
In the console:
```base
--------------------Proceeding  author  (based on publication) method--------------------
Searching about: Abramova
There is/are 3 result(s) founded on 1 page(s).
	|______ executing page 1: 3 items.: 100%|██████████| 3/3 [00:14<00:00,  4.81s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ...      Years
0  http://ifpni.org//author.htm?id=7EA48CBF-5871-...  ...  1915–2012
1  http://ifpni.org//author.htm?id=2D3693BB-A80D-...  ...  1935–2002
2  http://ifpni.org//author.htm?id=D8512DDF-D733-...  ...      1913–

[3 rows x 12 columns]
```

# Advanced functions
The nine function methods mentioned earlier correspond to the nine search methods on the IFPNI website portal. Building upon these basic methods, this Python package further provides additional advanced search methods, including searching for higher taxonomic groups of the target taxon, searching for lower taxonomic groups of the target taxon, searching for taxa published in the target publication, and searching for taxa and publications of the target paleobotanist.

There are 15 advanced functions.
## 10. supragenus_ancestors()
The function supragenus_ancestors() will start from the target taxon and recursively search for parent taxa at each higher level based on supragenus().
### 10.1. parameters of supragenus_ancestors()
This function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to supragenus(), you can view the list of available ranks in **Other information**.
### 10.2. supragenus_ancestors function example
Taking Orchidaceae as an example, the supragenus_ancestors() will search for parent taxa at each higher level of items that relate to "orchidaceae".
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

o2a = ifpni.supragenus_ancestors(name="orchidaceae")

print(o2a)

# save result to csv file
o2a.to_csv("./supragenus_ancestors_orchidaceae.csv")
```
In the console:
```base
--------------------Proceeding  ancestors of supragenus  (based on taxonomic) method--------------------
Searching about: orchidaceae
There is/are 2 result(s) founded on 1 page(s).
	|______ executing page 1: 2 items.: 100%|██████████| 2/2 [00:24<00:00, 12.46s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current fossil plant name is Orchidaceae**
		|____ Family Orchidaceae Juss. Gen. Pl. 64. 4 Aug 1789
			|____ Order Orchidales Raf.  Anal. Fam. Pl.: 56. 1815.
				|____ Class Liliopsida  Crantz, Inst. Rei Herb. 1: 461. 1766.
					|____ Phylum Magnoliophyta Reveal Phytologia, 1995, 79(2): 70. 29 Apr 1996

**Current fossil plant name is Protorchidaceae**
		|____ Family Protorchidaceae A. Massal. in Cantani Lotos, 9(1): 17. Jan 1859
			|____ Class Liliopsida  Crantz, Inst. Rei Herb. 1: 461. 1766.
				|____ Phylum Magnoliophyta Reveal Phytologia, 1995, 79(2): 70. 29 Apr 1996
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ...                                          Type href
0  http://ifpni.org//supragenus.htm?id=992C341F-8...  ...                                                NaN
1  http://ifpni.org//supragenus.htm?id=7DA9B270-1...  ...                                                NaN
2  http://ifpni.org//supragenus.htm?id=90554C13-B...  ...                                                NaN
3  http://ifpni.org//supragenus.htm?id=12AF6B1F-F...  ...  http://ifpni.org//genus.htm?id=D52E3FA4-C205-4...
4  http://ifpni.org//supragenus.htm?id=0604FB97-B...  ...  http://ifpni.org//genus.htm?id=C2D639DB-1CD0-4...
5  http://ifpni.org//supragenus.htm?id=90554C13-B...  ...                                                NaN
6  http://ifpni.org//supragenus.htm?id=12AF6B1F-F...  ...  http://ifpni.org//genus.htm?id=D52E3FA4-C205-4...

[7 rows x 27 columns]
```
## 11. genus_ancestors()
The function genus_ancestors() will start from the target taxon and recursively search for parent taxa at each higher level based on genus().
### 11.1. parameters of genus_ancestors()
his function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to genus(), you can view the list of available ranks in **Other information**.
### 11.2. genus_ancestors function example
Taking *achlys* as an example, the genus_ancestors() will search for parent taxa at each higher level of items that relate to "*achlys*".
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

a2a = ifpni.genus_ancestors(name="achlys")

print(a2a)

# save result to csv file
a2a.to_csv("./genus_ancestors_achlys.csv")
```
In the console:
```base
--------------------Proceeding  ancestors of genus  (based on taxonomic) method--------------------
Searching about: achlys
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:01<00:00,  1.67s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current fossil plant name is Achlys**
		|____ Genus Achlys DC.  Syst. Nat. 2: 35. Mai 1821.
			|____ Family Berberidaceae Juss. Gen. Pl. 286. 4 Aug 1789
				|____ Order Berberidales Bercht., J. Presl Přiroz. Rostl., Oddělení 1: 226. 15 Oct 1819
					|____ Class Magnoliopsida Brongn. Énum. Pl. Mus. Paris xxvi, 95. 5-12 Aug 1843
						|____ Phylum Magnoliophyta Reveal Phytologia, 1995, 79(2): 70. 29 Apr 1996
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ... Issue
0  http://ifpni.org//genus.htm?id=D30DF6EC-972F-D...  ...   NaN
1  http://ifpni.org//supragenus.htm?id=F14DD416-D...  ...   NaN
2  http://ifpni.org//supragenus.htm?id=08201C09-5...  ...   NaN
3  http://ifpni.org//supragenus.htm?id=483EB382-C...  ...   NaN
4  http://ifpni.org//supragenus.htm?id=12AF6B1F-F...  ...     2

[5 rows x 27 columns]
```
## 12. infragenus_ancestors()
The function infragenus_ancestors() will start from the target taxon and recursively search for parent taxa at each higher level based on infragenus().
### 12.1. parameters of infragenus_ancestors()
his function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to infragenus(), you can view the list of available ranks in **Other information**.
### 12.2. infragenus_ancestors function example
Taking *Stratiotes Imperfectus* as an example, the infragenus_ancestors() will search for parent taxa at each higher level of items that relate to "*Stratiotes Imperfectus*".
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

s2a = ifpni.infragenus_ancestors(name="Stratiotes Imperfectus")

print(s2a)

# save result to csv file
s2a.to_csv("./infragenus_ancestors_Stratiotes_Imperfectus.csv")
```
In the console:
```base
--------------------Proceeding  ancestors of infragenus  (based on taxonomic) method--------------------
Searching about: Stratiotes Imperfectus
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:02<00:00,  2.74s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current fossil plant name is Stratiotes Imperfectus**
		|____ Stratiotes Section Imperfectus V.P. Nikitin Paleokarp. Stratigr. Paleog. Neog. Aziatsk. Rossii ed. 2006 132. 30 Jan 2007
			|____ Genus Stratiotes L. Sp. Pl. 535. 1 May 1753
				|____ Family Hydrocharitaceae Juss. Gen. Pl. 67. 4 Aug 1789
					|____ Order Hydrocharitales Bercht., J. Presl Přiroz. Rostl., Oddělení 1: 271. 15 Oct 1819
						|____ Class Liliopsida  Crantz, Inst. Rei Herb. 1: 461. 1766.
							|____ Phylum Magnoliophyta Reveal Phytologia, 1995, 79(2): 70. 29 Apr 1996
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ... Issue
0  http://ifpni.org//infragenus.htm?id=1FE5B745-E...  ...   NaN
1  http://ifpni.org//genus.htm?id=7C607A95-D84A-4...  ...   NaN
2  http://ifpni.org//supragenus.htm?id=C24811A6-5...  ...   NaN
3  http://ifpni.org//supragenus.htm?id=0873C10C-C...  ...   NaN
4  http://ifpni.org//supragenus.htm?id=90554C13-B...  ...   NaN
5  http://ifpni.org//supragenus.htm?id=12AF6B1F-F...  ...     2

[6 rows x 29 columns]
```
## 13. species_ancestors()
The function species_ancestors() will start from the target taxon and recursively search for parent taxa at each higher level based on species().
### 13.1. parameters of species_ancestors()
his function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to species(), you can view the list of available ranks in **Other information**.
- *paleoregion_list*: (Default:None) choose the paleoregions available to species(), you can view the list of available paleoregions in **Other information**.
### 13.2. species_ancestors function example
Taking *Cordaites acadianus* as an example, the infragenus_ancestors() will search for parent taxa at each higher level of items that relate to "*Cordaites acadianus*".
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

c2a = ifpni.species_ancestors(name="Cordaites acadianus")

print(c2a)

# save result to csv file
c2a.to_csv("./species_ancestors_cordaites_acadianus.csv")
```
In the console:
```base
--------------------Proceeding  ancestors of species  (based on taxonomic) method--------------------
Searching about: Cordaites acadianus
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:01<00:00,  1.22s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current fossil plant name is Cordaites acadianus**
		|____ Cordaites acadianus (Dawson) Knowlt. Proc. U.S. Natl. Mus., 45(1994): 608. 21 Jun 1913
			|____ Genus Cordaites Unger Gen. Sp. Pl. Foss. 277. 18 Apr 1850
				|____ Family Cordaitaceae Grand'Eury Mém. Divers Savants Acad. Roy. Sci. Inst. Roy. France, Sci. Math., 24(1): 270, 313, 317. Apr 1876
					|____ Order Cordaitales Campb. Univ. Text-book Bot. 346, 326. 11 Apr 1902
						|____ Class Cordaitopsida Lesq. Sec. Geol. Surv. Pennsylvania Rept. Progr., 1880, P(2): iv, 525. 21 Jan 1881
							|____ Phylum Cordaitophyta Wilh. Bock Geol. Center Res. Ser., 2: 254. 19 Nov 1962
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ... Annee/Jahrgang
0  http://ifpni.org//species.htm?id=3C6A4B88-0B69...  ...            NaN
1  http://ifpni.org//genus.htm?id=4A970E78-EF37-4...  ...            NaN
2  http://ifpni.org//supragenus.htm?id=24D808B2-5...  ...            NaN
3  http://ifpni.org//supragenus.htm?id=ED80BA57-2...  ...            NaN
4  http://ifpni.org//supragenus.htm?id=B08743B2-F...  ...           1880
5  http://ifpni.org//supragenus.htm?id=6683AB52-6...  ...            NaN

[6 rows x 29 columns]
```
## 14. infraspecies_ancestors()
The function infraspecies_ancestors() will start from the target taxon and recursively search for parent taxa at each higher level based on infraspecies().
### 14.1. parameters of infraspecies_ancestors()
his function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to infraspecies(), you can view the list of available ranks in **Other information**.
- *paleoregion_list*: (Default:None) choose the paleoregions available to infraspecies(), you can view the list of available paleoregions in **Other information**.
### 14.2. infraspecies_ancestors function example
Taking *Populus balsamoides minor* as an example, the infragenus_ancestors() will search for parent taxa at each higher level of items that relate to "*Populus balsamoides minor*".
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

p2a = ifpni.infraspecies_ancestors(name="Populus balsamoides minor")

print(p2a)

# save result to csv file
p2a.to_csv("./infraspecies_ancestors_populus_balsamoides_minor.csv")
```
In the console:
```base
--------------------Proceeding  ancestors of infraspecies  (based on taxonomic) method--------------------
Searching about: Populus balsamoides minor
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:06<00:00,  6.09s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current fossil plant name is Populus balsamoides minor**
		|____ Populus balsamoides Varietas minor Wentzel Sitzungsber. Kaiserl. Akad. Wiss., Wien, Math.-Naturwiss. Cl., Abt. 1, 83(3): 250. 14 Jul 1881
			|____ Populus balsamoides Goepp. Tert. Fl. Schossnitz 23. 1-2 Mar 1855
				|____ Genus Populus L. Sp. Pl. 1034. 1 May 1753
					|____ Family Salicaceae Mirb.  Élém. Phys. Vég. Bot. 2: 905. 1815.
						|____ Order Samydales Bercht., J. Presl Přiroz. Rostl., Oddělení 1: 227. 15 Oct 1819
							|____ Class Magnoliopsida Brongn. Énum. Pl. Mus. Paris xxvi, 95. 5-12 Aug 1843
								|____ Phylum Magnoliophyta Reveal Phytologia, 1995, 79(2): 70. 29 Apr 1996
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ... Annee/Jahrgang
0  http://ifpni.org//infraspecies.htm?id=CB3368E6...  ...            NaN
1  http://ifpni.org//species.htm?id=A8D592E5-82FE...  ...            NaN
2  http://ifpni.org//genus.htm?id=496CBC11-3CE8-4...  ...            NaN
3  http://ifpni.org//supragenus.htm?id=C0444EDD-F...  ...            NaN
4  http://ifpni.org//supragenus.htm?id=B98D3D8F-A...  ...            NaN
5  http://ifpni.org//supragenus.htm?id=483EB382-C...  ...            NaN
6  http://ifpni.org//supragenus.htm?id=12AF6B1F-F...  ...           1995

[7 rows x 42 columns]
```
## 15. supragenus_descendants()
The function supragenus_descendants() will start from the target taxon and recursively search for descendant taxa at each lower level based on supragenus().
### 15.1. parameters of supragenus_descendants()
his function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to supragenus(), you can view the list of available ranks in **Other information**.
### 15.2. supragenus_descendants function example
Taking orchidaceae as an example, the supragenus_descendants() will search for descendant taxa at each lower level of items that relate to orchidaceae.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

o2d = ifpni.supragenus_descendants(name='orchidaceae')

print(o2d)

# save result to csv file
o2d.to_csv("./supragenus_descendants_orchidaceae.csv")
```
In the console:
```base
--------------------Proceeding  descendants of supragenus  (based on taxonomic) method--------------------
Searching about: orchidaceae
There is/are 2 result(s) founded on 1 page(s).
	|______ executing page 1: 2 items.: 100%|██████████| 2/2 [00:03<00:00,  1.81s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current fossil plant name is Orchidaceae**
		|____ Family Orchidaceae Juss. Gen. Pl. 64. 4 Aug 1789
			|____ Genus Annulites Poinar Amer. Entomol. (Lanham), 62(3): 174. 8 Aug 2016
				|____ Annulites mexicanus Poinar Amer. Entomol. (Lanham), 62(3): 174. 8 Aug 2016
			|____ Genus Cylindrocites Poinar Amer. Entomol. (Lanham), 62(3): 172. 8 Aug 2016
				|____ Cylindrocites brownii Poinar Amer. Entomol. (Lanham), 62(3): 173. 8 Aug 2016
			|____ Genus Globosites Poinar Neues Jahrb. Geol. Paläontol., Abh., 279(3): 289. Mar 2016
				|____ Globosites apicola Poinar Neues Jahrb. Geol. Paläontol., Abh., 279(3): 289. Mar 2016
			|____ Genus Mycophoris Poinar Bot. (Canada), 2017, 95(1): 2. 30 Nov 2016
				|____ Mycophoris elongatus Poinar Bot. (Canada), 2017, 95(1): 2. 30 Nov 2016
			|____ Genus Rudiculites Poinar Neues Jahrb. Geol. Paläontol., Abh., 279(3): 289. Mar 2016
				|____ Rudiculites dominicanus Poinar Neues Jahrb. Geol. Paläontol., Abh., 279(3): 289. Mar 2016
			|____ Genus Succinanthera Poinar, F.N. Rasm. Bot. J. Linn. Soc., 183(3): 328. 29 Mar 2017
				|____ Succinanthera baltica Poinar, F.N. Rasm. Bot. J. Linn. Soc., 183(3): 328. 29 Mar 2017

**Current fossil plant name is Protorchidaceae**
		|____ Family Protorchidaceae A. Massal. in Cantani Lotos, 9(1): 17. Jan 1859
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                 href  ...                                Authors (Name) href
0   http://ifpni.org//supragenus.htm?id=992C341F-8...  ...                                                NaN
1   http://ifpni.org//genus.htm?id=1E8B4104-0CDD-8...  ...                                                NaN
2   http://ifpni.org//species.htm?id=4EEAC220-0533...  ...                                                NaN
3   http://ifpni.org//genus.htm?id=BFBFED2C-8771-E...  ...                                                NaN
4   http://ifpni.org//species.htm?id=9C1D126C-D389...  ...                                                NaN
5   http://ifpni.org//genus.htm?id=D4417593-5254-A...  ...                                                NaN
6   http://ifpni.org//species.htm?id=D0ABFFC8-A78D...  ...                                                NaN
7   http://ifpni.org//genus.htm?id=337E730E-E061-B...  ...                                                NaN
8   http://ifpni.org//species.htm?id=6C58C85C-5C7D...  ...                                                NaN
9   http://ifpni.org//genus.htm?id=38143F06-07D8-6...  ...                                                NaN
10  http://ifpni.org//species.htm?id=10CC7E63-5E75...  ...                                                NaN
11  http://ifpni.org//genus.htm?id=EBE4CB2C-72A6-4...  ...                                                NaN
12  http://ifpni.org//species.htm?id=DB660924-19E0...  ...                                                NaN
13  http://ifpni.org//supragenus.htm?id=0604FB97-B...  ...  http://ifpni.org//author.htm?id=7963DCD6-7C5D-...

[14 rows x 40 columns]
```
## 16. genus_descendants()
The function genus_descendants() will start from the target taxon and recursively search for descendant taxa at each lower level based on genus().
### 16.1. parameters of genus_descendants()
his function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to genus(), you can view the list of available ranks in **Other information**.
### 16.2. genus_descendants function example
Taking *alloberberis* as an example, the genus_descendants() will search for descendant taxa at each lower level of items that relate to *alloberberis*.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

a2d = ifpni.genus_descendants(name='alloberberis')

print(a2d)

# save result to csv file
a2d.to_csv("./genus_descendants_alloberberis.csv")
```
In the console:
```base
--------------------Proceeding  descendants of genus  (based on taxonomic) method--------------------
Searching about: alloberberis
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:01<00:00,  1.76s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current fossil plant name is Alloberberis**
		|____ Genus Alloberberis C.C. Yu, K.F. Chung Taxon, 66(6): 1385. 22 Dec 2017
			|____ Alloberberis aceroides (Knowlt.) Doweld Phytotaxa, 351(1): 73. 29 May 2018
			|____ Alloberberis axelrodii Doweld Phytotaxa, 351(1): 73. 29 May 2018
			|____ Alloberberis bilinica (Unger) Doweld Phytotaxa, 351(1): 73. 29 May 2018
			|____ Alloberberis caeruleomontana Doweld Phytotaxa, 351(1): 74. 29 May 2018
			|____ Alloberberis lobodonta (H.F. Becker) Doweld Phytotaxa, 351(1): 74. 29 May 2018
			|____ Alloberberis marginata (Lesq.) Doweld Phytotaxa, 351(1): 74. 29 May 2018
			|____ Alloberberis obliqua (MacGinitie) Doweld Phytotaxa, 351(1): 74. 29 May 2018
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ...                                          Pub. href
0  http://ifpni.org//genus.htm?id=542ACE50-1F15-E...  ...                                                NaN
1  http://ifpni.org//species.htm?id=7B7E64DF-C2D1...  ...                                                NaN
2  http://ifpni.org//species.htm?id=72DD25B8-5D3C...  ...  http://ifpni.org//publication.htm?id=D71AB0AF-...
3  http://ifpni.org//species.htm?id=0B00BB8C-D828...  ...                                                NaN
4  http://ifpni.org//species.htm?id=CD233A02-156D...  ...  http://ifpni.org//publication.htm?id=B68B198B-...
5  http://ifpni.org//species.htm?id=DC2EBBE5-2AB4...  ...                                                NaN
6  http://ifpni.org//species.htm?id=2B4BA7A5-1B1F...  ...                                                NaN
7  http://ifpni.org//species.htm?id=1B2519F4-5DDC...  ...                                                NaN

[8 rows x 32 columns]
```
## 17. infragenus_descendants()
The function infragenus_descendants() will start from the target taxon and recursively search for descendant taxa at each lower level based on infragenus().
### 17.1. parameters of infragenus_descendants()
his function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to infragenus(), you can view the list of available ranks in **Other information**.
### 17.2. infragenus_descendants function example
Taking *Gleicheniidites Triplexisporis* as an example, the infragenus_descendants() will search for descendant taxa at each lower level of items that relate to *Gleicheniidites Triplexisporis*.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

g2d = ifpni.infragenus_descendants(name="Gleicheniidites Triplexisporis")

print(g2d)

# save result to csv file
g2d.to_csv("./infragenus_descendants_gleicheniidites_triplexisporis.csv")
```
In the console:
```base
--------------------Proceeding  descendants of infragenus  (based on taxonomic) method--------------------
Searching about: Gleicheniidites Triplexisporis
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:01<00:00,  1.27s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current fossil plant name is Gleicheniidites Triplexisporis**
		|____ Gleicheniidites Subgenus Triplexisporis Krutzsch Beih. Z. Geol., (21-22): 114. Apr 1959
			|____ Gleicheniidites nigrus (Bolkh.) Krutzsch Beih. Z. Geol., (21-22): 114. Apr 1959
			|____ Gleicheniidites triplex (Bolkh.) Krutzsch Beih. Z. Geol., (21-22): 114. Apr 1959
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ...                              Вasionym Species href
0  http://ifpni.org//infragenus.htm?id=D20F3A29-8...  ...                                                NaN
1  http://ifpni.org//species.htm?id=37D7160A-AEB9...  ...  http://ifpni.org//species.htm?id=BCF92924-D7C9...
2  http://ifpni.org//species.htm?id=A3008BE4-1948...  ...  http://ifpni.org//species.htm?id=E8E3E2FB-3E6E...

[3 rows x 23 columns]
```
## 18. species_descendants()
The function species_descendants() will start from the target taxon and recursively search for descendant taxa at each lower level based on species().
### 18.1. parameters of species_descendants()
his function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to species(), you can view the list of available ranks in **Other information**.
- *paleoregion_list*: (Default:None) choose the paleoregions available to species(), you can view the list of available paleoregions in **Other information**.
### 18.2. species_descendants function example
Taking *Cordaites acadianus* as an example, the species_descendants() will search for descendant taxa at each lower level of items that relate to *Cordaites acadianus*.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

c2d = ifpni.species_descendants(name='Cordaites acadianus')

print(c2d)

# save result to csv file
c2d.to_csv("./species_descendants_cordaites_acadianus.csv")
```
In the console:
```base
--------------------Proceeding  descendants of species  (based on taxonomic) method--------------------
Searching about: Cordaites acadianus
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:03<00:00,  3.90s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current fossil plant name is Cordaites acadianus**
		|____ Cordaites acadianus (Dawson) Knowlt. Proc. U.S. Natl. Mus., 45(1994): 608. 21 Jun 1913
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ...  Year
0  http://ifpni.org//species.htm?id=3C6A4B88-0B69...  ...  1913

[1 rows x 19 columns]
```
## 19. infraspecies_descendants()
The function infraspecies_descendants() will start from the target taxon and recursively search for descendant taxa at each lower level based on infraspecies().
### 19.1. parameters of infraspecies_descendants()
his function contains several parameters as below:
- *name*: (Required) the name of taxa that you interested.
- *first_symbols*: (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["name","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *rank_list*: (Default:None) choose the ranks available to infraspecies(), you can view the list of available ranks in **Other information**.
- *paleoregion_list*: (Default:None) choose the paleoregions available to infraspecies(), you can view the list of available paleoregions in **Other information**.
### 19.2. infraspecies_descendants function example
Taking *Populus balsamoides minor* as an example, the infraspecies_descendants() will search for descendant taxa at each lower level of items that relate to *Populus balsamoides minor*.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

p2d = ifpni.infraspecies_descendants(name='Populus balsamoides minor')

print(p2d)

# save result to csv file
p2d.to_csv("./infraspecies_descendants_populus_balsamoides_minor.csv")
```
In the console:
```base
--------------------Proceeding  descendants of infraspecies  (based on taxonomic) method--------------------
Searching about: Populus balsamoides minor
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:01<00:00,  1.64s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current fossil plant name is Populus balsamoides minor**
		|____ Populus balsamoides Varietas minor Wentzel Sitzungsber. Kaiserl. Akad. Wiss., Wien, Math.-Naturwiss. Cl., Abt. 1, 83(3): 250. 14 Jul 1881
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ...                                          Pub. href
0  http://ifpni.org//infraspecies.htm?id=CB3368E6...  ...  http://ifpni.org//publication.htm?id=817AFF7D-...

[1 rows x 24 columns]
```
## 20. publication2taxon()
The function publication2taxon() will retrieve all published records from all types of publications, including books, journal articles, conference proceedings, reports, theses that return by publication() method first.
### 20.1. parameters of publication2taxon()
his function contains several parameters as below:
- *title*: (Required) the name of publication that you interested.
- *first_symbols*:  (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["title","yearFrom"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *author*: (Default:None) only return items authorized by given author.
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
- *journal*: (Default: None) only return items published by given journal.
### 20.2. publication2taxon function example
Taking "A brief review of the stratigraphy and floral succession of the Carboniferous in NW. Spain" as an example, the publication2taxon() will search for published taxa from target publication.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

p2t = ifpni.publication2taxon(title='A brief review of the stratigraphy and floral succession of the Carboniferous in NW. Spain')
    
print(p2t)

# save result to csv file
p2t.to_csv("./publication2taxon_A_brief.csv")
```
In the console:
```base
--------------------Proceeding  taxon names of publication  (based on publication) method--------------------
Searching about: A brief review of the stratigraphy and floral succession of the Carboniferous in NW. Spain
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:02<00:00,  2.88s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current publication name is A brief review of the stratigraphy and floral succession of the Carboniferous in NW. Spain**
		|____ A brief review of the stratigraphy and floral succession of the Carboniferous in NW. Spain
			|____ Rhodeopteridium
			|____ Callipteridium densinervium
			|____ Callipteridium zeilleri
			|____ Neuropteris asturiana
			|____ Pecopteris jongmansii
			|____ Pecopteris melendezii
			|____ Pecopteris parallelolobata
			|____ Pecopteris triangularis
			|____ Polymorphopteris multifurcata
			|____ Rhodea jongmansii
			|____ Rhodeopteridium jongmansii
			|____ Sphenopteris stockmansii
			|____ Validopteris hispanica
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                 href  ...                                             Descr.
0   http://ifpni.org//publication.htm?id=2C5CB809-...  ...                                                NaN
1   http://ifpni.org//genus.htm?id=235465F5-8290-0...  ...                                                NaN
2   http://ifpni.org//species.htm?id=11584F1E-4B2F...  ...                                                NaN
3   http://ifpni.org//species.htm?id=7562B29A-24EB...  ...                                                NaN
4   http://ifpni.org//species.htm?id=BDA4BF3B-45C4...  ...                                                NaN
5   http://ifpni.org//species.htm?id=62FE32D2-812C...  ...                                                NaN
6   http://ifpni.org//species.htm?id=E88ECA8C-DD7F...  ...                                                NaN
7   http://ifpni.org//species.htm?id=551A5FA3-E11D...  ...                                                NaN
8   http://ifpni.org//species.htm?id=EE772AA1-46DE...  ...                                                NaN
9   http://ifpni.org//species.htm?id=A90D70E5-4B21...  ...                                                NaN
10  http://ifpni.org//species.htm?id=436FFC00-2D6D...  ...   originally incorrectly designated as a 'syntype'
11  http://ifpni.org//species.htm?id=2792989E-351C...  ...   originally incorrectly designated as a 'syntype'
12  http://ifpni.org//species.htm?id=AF2F3DB4-A540...  ...  Sphenopteris sp. in STOCKMANS & WILLIERE, 1952...
13  http://ifpni.org//species.htm?id=5EC26CC2-DEF1...  ...                                                NaN

[14 rows x 42 columns]
```
## 21. book2taxon()
The function book2taxon() will retrieve all published records from books that return by book() method first.
### 21.1. parameters of book2taxon()
This function contains several parameters as below:
- *title*: (Required) the name of publication that you interested.
- *first_symbols*:  (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["title","titleOrigin","titleAbbr"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *abbreviation*: (Default:None) only return items that has the given abbreviation.
### 21.2. book2taxon function example
Taking "100 Jahre Arboretum Berlin" as an example, the book2taxon() will search for published taxa from target book(s).
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

j2t = ifpni.book2taxon(title='100 Jahre Arboretum Berlin')

print(j2t)

# save result to csv file
j2t.to_csv("./book2taxon_100.csv")
```
In the console:
```base
--------------------Proceeding  taxon names of book  (based on publication) method--------------------
Searching about: 100 Jahre Arboretum Berlin
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:00<00:00,  1.23it/s]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current publication name is 100 Jahre Arboretum Berlin**
		|____ 100 Jahre Arboretum Berlin
			|____ Calamiten aus dem Oberkarbon und Rotliegenden des Thüringer Waldes
				|____ Palaeostachya thuringiaca
				|____ Brukmannia tuberculata
				|____ Poacites zeiformis
				|____ Stachannularia thuringiaca
				|____ Zamites schlotheimii
			|____ Zur Bedeutung von Relikten in der Florengeschichte
				|____ Decaisnea bornensis
				|____ Euscaphis pietzschii
				|____ Poliothyrsis czornegosdensis
				|____ Poliothyrsis eurorimosa
				|____ Poliothyrsis hercynica
				|____ Poliothyrsis lutetianoides
				|____ Poliothyrsis rimosa
				|____ Tapiscia chandlerae
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                 href  ...                      Descr.
0   http://ifpni.org//book.htm?id=176850CE-A9C2-40...  ...                         NaN
1   http://ifpni.org//publication.htm?id=2DC16184-...  ...                         NaN
2   http://ifpni.org//species.htm?id=1E25BFA1-0E8B...  ...                         NaN
3   http://ifpni.org//species.htm?id=2953B26F-14D7...  ...                         NaN
4   http://ifpni.org//species.htm?id=CB5DFEF0-E600...  ...                         NaN
5   http://ifpni.org//species.htm?id=A190E02A-6C1A...  ...                         NaN
6   http://ifpni.org//species.htm?id=4623925C-A69C...  ...  ut "Cycadites zamiifolius"
7   http://ifpni.org//publication.htm?id=8B4F5FC7-...  ...                         NaN
8   http://ifpni.org//species.htm?id=0E579782-E1EF...  ...                         NaN
9   http://ifpni.org//species.htm?id=91F33BF4-7422...  ...                         NaN
10  http://ifpni.org//species.htm?id=32251F6B-4A64...  ...                         NaN
11  http://ifpni.org//species.htm?id=EF248775-BBC9...  ...                         NaN
12  http://ifpni.org//species.htm?id=04082E9B-B410...  ...                         NaN
13  http://ifpni.org//species.htm?id=844DC653-FCB7...  ...                         NaN
14  http://ifpni.org//species.htm?id=FB669A30-2D28...  ...                         NaN
15  http://ifpni.org//species.htm?id=17660F20-8CB2...  ...                         NaN

[16 rows x 55 columns]
```
## 22. journal2taxon()
The function journal2taxon() will retrieve all published records from journal that return by journal() method first.
### 22.1. parameters of journal2taxon()
This function contains several parameters as below:
- *title*: (Required) the name of publication that you interested.
- *first_symbols*:  (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["title","titleOrigin"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
- *original_spelling*: (Default:None) only return items that has the given original spelling.
- *yearFrom*: (Default:None) decide the minimum published year of items.
- *yearTo*: (Default:None) decide the maximum published year of items.
### 22.2. journal2taxon function example
Taking "Acta Palaeontologica Polonica" as an example, the journal2taxon() will search for published taxa from target journal(s).
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

a2t = ifpni.journal2taxon(title="Acta Palaeontologica Polonica")

print(a2t)

# save result to csv file
a2t.to_csv("./journal2taxon_acta_palaeontologica)polonica.csv")
```
In the console:
```base
--------------------Proceeding  taxon names of journal  (based on publication) method--------------------
Searching about: Acta Palaeontologica Polonica
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:01<00:00,  1.28s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Current publication name is Acta Palaeontologica Polonica**
		|____ Acta Palaeontologica Polonica
			|____ A new species of Todites (Pteridophyta) with in situ spores from the Upper Permian of Pechora Cis-Urals (Russia)
				|____ Todites lobulatus
			|____ Coccolithophoridae z górnego mastrychtu Polski środkowej
				|____ Cribrosphaerella
				|____ Dictyolithus
				|____ Nephrolithus
				|____ Cribrosphaerella ehrenbergii
				|____ Discolithus cretaceus
				|____ Discolithus numerosus
			|____ Latest Cretaceous leaf floras from south-eastern Poland and western Ukraine
				|____ Debeya Dewalquea
				|____ Araliopsoides minor
				|____ Debeya paulinae
				|____ Dicotylophyllum varienerve
				|____ Dicotylophyllum zubraense
				|____ Ettingshausenia lublinensis
				|____ Rarytkinia polonica
				|____ Dewalquea insignis
			|____ New species of megaspores from the Trias of Poland
				|____ Bothriotriletes
				|____ Otynisporites
				|____ Aneuletes acrochordonodes
				|____ Aneuletes clavatus
				|____ Aneuletes pomeranus
				|____ Bacutriletes corynactiformis
				|____ Bacutriletes costatispinosus
				|____ Bacutriletes micros
				|____ Bacutriletes pseudoreticulatus
				|____ Bothriotriletes grandis
				|____ Dijkstraisporites capillatus
				|____ Echitriletes latispinosus
				|____ Echitriletes pectinatus
				|____ Echitriletes prerussus
				|____ Erlansonisporites licheniformis
				|____ Horstisporites bertelsenii
				|____ Horstisporites irregularis
				|____ Horstisporites nidzicensis
				|____ Hughesisporites simplex
				|____ Maexisporites megnuszewensis
				|____ Maexisporites ooliticus
				|____ Maexisporites spongiosus
				|____ Nathorstisporites invenustus
				|____ Otynisporites eotriassicus
				|____ Otynisporites tuberculatus
				|____ Pusulosporites permotriassicus
				|____ Tenellisporites planispinosus
				|____ Triangulatisporites reticulatus
				|____ Triangulatisporites tuberculatus
				|____ Trileites crassitectatus
				|____ Trileites flexuosus
				|____ Verrutriletes preutilis
			|____ On two Ordovician calcareous algae
				|____ Vermiporella fragilis
			|____ Palynological characteristics of the Neogene of Western Poland
				|____ Iteapollis
				|____ Iteapollis angustiporatus
				|____ Microfoveolatisporis minutus
				|____ Porocolpopollenites maturus
				|____ Tricolporopollenites indeterminatus
			|____ Revision of the Late Cretaceous genus Mongolichara Kyansep-Romaschkina
				|____ Lamprothamnium bugintsavicum
				|____ Mongolichara aurea
				|____ Mongolichara gobica
			|____ Some new megaspore species of the Triassic of Poland
				|____ Aneuletes porosus
				|____ Bacutriletes decipiens
				|____ Erlansonisporites lobatus
				|____ Erlansonisporites micros
				|____ Hughesisporites calvescens
				|____ Narkisporites digitiformis
				|____ Trileites robustus
			|____ The early angiosperm Pseudoasterophyllites cretaceus from Albian-Cenomanian of Czech Republic and France revisited
				|____ Pseudoasterophyllites cretaceus
			|____ The Upper Triassic flora of Svalbard
				|____ Arberophyllum substrictum
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                 href  ...                                             Descr.
0   http://ifpni.org//journal.htm?id=6357910E-D63C...  ...                                                NaN
1   http://ifpni.org//publication.htm?id=AEE924B5-...  ...                                                NaN
2   http://ifpni.org//species.htm?id=F645F297-49D5...  ...                                                NaN
3   http://ifpni.org//publication.htm?id=1030F7C0-...  ...                                                NaN
4   http://ifpni.org//genus.htm?id=3DF41BE7-8D24-4...  ...                                                NaN
..                                                ...  ...                                                ...
71  http://ifpni.org//species.htm?id=7A1A4EB3-E56B...  ...                                                NaN
72  http://ifpni.org//publication.htm?id=3387CC27-...  ...                                                NaN
73  http://ifpni.org//species.htm?id=089093AD-C39E...  ...  Pecínov, Peruc-Korycany Formation, unit 5, Cze...
74  http://ifpni.org//publication.htm?id=96D3A75D-...  ...                                                NaN
75  http://ifpni.org//species.htm?id=88CC0B23-A938...  ...                                                NaN

[76 rows x 60 columns]
```
## 23. author2publication()
This function author2publication() allows users to retrieve publications authorised by specific paleobotanists.
### 23.1. parameters of author2publication()
This function contains several parameters as below:
- *lastName*: (Required) the name of paleobotanist that you interested.
- *first_symbols*:  (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["lastName"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
### 23.2. author2publication() function example
Taking "Abramova" as an example, the author2publication() will search for all publications authorised by paleobotnists whose name relates to Abramova.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

a2p = ifpni.author2publication(lastName='Abramova')

print(a2p)

# save result to csv file
a2p.to_csv("./author2publication_abramova.csv")
```
In the console:
```base
--------------------Proceeding  publication of author  (based on author) method--------------------
Searching about: Abramova
There is/are 7 result(s) founded on 1 page(s).
	|______ executing page 1: 7 items.: 100%|██████████| 7/7 [00:12<00:00,  1.75s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                href  ... Volume
0  http://ifpni.org//publication.htm?id=C7A1074D-...  ...    NaN
1  http://ifpni.org//publication.htm?id=6DDA53EC-...  ...    NaN
2  http://ifpni.org//publication.htm?id=020F31A7-...  ...     27
3  http://ifpni.org//publication.htm?id=7711E46A-...  ...    NaN
4  http://ifpni.org//publication.htm?id=84F4E50F-...  ...    NaN
5  http://ifpni.org//publication.htm?id=EB4CBF32-...  ...    NaN
6  http://ifpni.org//publication.htm?id=79162F21-...  ...    NaN

[7 rows x 26 columns]
```
## 24. author2taxon()
This function author2taxon() allows users to retrieve plant taxa authorised by specific paleobotanist.
### 24.1. parameters of author2taxon()
This function contains several parameters as below:
- *lastName*: (Required) the name of paleobotanist that you interested.
- *first_symbols*:  (Default:False) decide whether search items only by first symbols.
- *order*: (Default:None) decide the result in order by any one from the list ["lastName"]
- *orderDirection*: (Default:None) decide the order direction of result by any one of the list["desc","asc"]
### 24.2. author2taxon() function example
Taking "Abramova" as an example, the author2taxon() will search for all taxa authorised by paleobotnists whose name relates to Abramova.
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

a2t = ifpni.author2taxon(lastName='Abramova')

print(a2t)

# save result to csv file
a2t.to_csv("./author2taxon_abramova.csv")
```
In the console:
```base
--------------------Proceeding  taxon names of author  (based on author) method--------------------
Searching about: Abramova
--------------------Proceeding  supragenus  (based on taxonomic) method--------------------
Searching about: 
There is/are 0 result(s) founded on 0 page(s).
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
--------------------Proceeding  genus  (based on taxonomic) method--------------------
Searching about: 
There is/are 2 result(s) founded on 1 page(s).
	|______ executing page 1: 2 items.: 100%|██████████| 2/2 [00:02<00:00,  1.49s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
--------------------Proceeding  infragenus  (based on taxonomic) method--------------------
Searching about: 
There is/are 0 result(s) founded on 0 page(s).
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
--------------------Proceeding  species  (based on taxonomic) method--------------------
Searching about: 
There is/are 16 result(s) founded on 2 page(s).
	|______ executing page 1: 10 items.: 100%|██████████| 10/10 [00:24<00:00,  2.45s/it]
	|______ executing page 2: 6 items.: 100%|██████████| 6/6 [00:22<00:00,  3.72s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
--------------------Proceeding  infraspecies  (based on taxonomic) method--------------------
Searching about: 
There is/are 1 result(s) founded on 1 page(s).
	|______ executing page 1: 1 items.: 100%|██████████| 1/1 [00:01<00:00,  1.81s/it]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                 href  ...                                       Species href
0   http://ifpni.org//genus.htm?id=0C5DF68C-93FF-4...  ...                                                NaN
1   http://ifpni.org//genus.htm?id=D15E1A6B-DA3E-4...  ...                                                NaN
2   http://ifpni.org//species.htm?id=FC20164D-B8CF...  ...                                                NaN
3   http://ifpni.org//species.htm?id=95280C3D-EF76...  ...                                                NaN
4   http://ifpni.org//species.htm?id=1738C356-C0DA...  ...                                                NaN
5   http://ifpni.org//species.htm?id=2A0F65A4-5727...  ...                                                NaN
6   http://ifpni.org//species.htm?id=4A1BA331-BB7E...  ...                                                NaN
7   http://ifpni.org//species.htm?id=03E4E195-7DB3...  ...                                                NaN
8   http://ifpni.org//species.htm?id=89FA7886-32BF...  ...                                                NaN
9   http://ifpni.org//species.htm?id=B8D1D980-AAF3...  ...                                                NaN
10  http://ifpni.org//species.htm?id=297CA159-3FCC...  ...                                                NaN
11  http://ifpni.org//species.htm?id=1E21BDC1-0A01...  ...                                                NaN
12  http://ifpni.org//species.htm?id=E1E56C92-3F8A...  ...                                                NaN
13  http://ifpni.org//species.htm?id=B13718AD-0223...  ...                                                NaN
14  http://ifpni.org//species.htm?id=263D9C26-858F...  ...                                                NaN
15  http://ifpni.org//species.htm?id=08DCBCF9-CD42...  ...                                                NaN
16  http://ifpni.org//species.htm?id=B734AA78-68B1...  ...                                                NaN
17  http://ifpni.org//species.htm?id=36F9FD88-8B33...  ...                                                NaN
18  http://ifpni.org//infraspecies.htm?id=A619DB93...  ...  http://ifpni.org//species.htm?id=20459D7C-39A9...

[19 rows x 44 columns]
```



# Other information
## Available rank hierarchy lists for different functions
If you want to check rank lists of all five basic functions based on taxonomic hierarchy, you can use available_rank():
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

ifpni.available_rank()
```
In the console:
```base
Available rank list for supragenus:
	 ['Regnum', 'Subregnum', 'Phylum', 'Subphylum', 'Superphylum', 'Class', 'Subclass', 'Superclass', 'Infraclass', 'Order', 'Superorder', 'Suborder', 'Infraorder', 'Family', 'Superfamily', 'Subfamily', 'Infrafamily', 'Tribe', 'Supertribe', 'Supersubtribe', 'Subtribe', 'Infratribe', 'Turma', 'Anteturma', 'Suprasubturma', 'Subturma', 'Infraturma', 'Unranked']
Available rank list for genus:
	 ['Genus', 'Supergenus', 'Group', 'Subgroup', 'Unranked']
Available rank list for infragenus:
	 ['Genus', 'Infragenus', 'Subgenus', 'Section', 'Subsection', 'Supersection', 'Series', 'Subseries', 'Superseries', 'Unranked']
Available rank list for species:
	 ['Species', 'Superspecies', 'Unranked']
Available rank list for infraspecies:
	 ['Subspecies', 'Supervarietas', 'Varietas', 'Subvarietas', 'Forma', 'Subforma', 'Infraspecies', 'Unranked']
```
Also, you can check rank list of specific function as below,
### rank of supragenus
You can check the available ranks of *supragenus* function by typing:
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

ifpni.available_rank(method="supragenus")
```
Then you will see:
```base
Available rank list for supragenus:
	 ['Regnum', 'Subregnum', 'Phylum', 'Subphylum', 'Superphylum', 'Class', 'Subclass', 'Superclass', 'Infraclass', 'Order', 'Superorder', 'Suborder', 'Infraorder', 'Family', 'Superfamily', 'Subfamily', 'Infrafamily', 'Tribe', 'Supertribe', 'Supersubtribe', 'Subtribe', 'Infratribe', 'Turma', 'Anteturma', 'Suprasubturma', 'Subturma', 'Infraturma', 'Unranked']
```

### rank of genus
You can check the available ranks of *genus* function by typing:
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

ifpni.available_rank(method="genus")
```
Then you will see:
```base
Available rank list for genus:
	 ['Genus', 'Supergenus', 'Group', 'Subgroup', 'Unranked']
```
### rank of infragenus
You can check the available ranks of *infragenus* function by typing:
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

ifpni.available_rank(method="infragenus")
```
Then you will see:
```base
Available rank list for infragenus:
	 ['Genus', 'Infragenus', 'Subgenus', 'Section', 'Subsection', 'Supersection', 'Series', 'Subseries', 'Superseries', 'Unranked']
```
### rank of species
You can check the available ranks of *species* function by typing:
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

ifpni.available_rank(method="species")
```
Then you will see:
```base
Available rank list for species:
	 ['Species', 'Superspecies', 'Unranked']
```
### rank of infraspecies
You can check the available ranks of *infraspecies* function by typing:
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

ifpni.available_rank(method="infraspecies")
```
Then you will see:
```base
Available rank list for infraspecies:
	 ['Subspecies', 'Supervarietas', 'Varietas', 'Subvarietas', 'Forma', 'Subforma', 'Infraspecies', 'Unranked']
```
## Available paleoregion list for species() and infraspecies()
You can check the available paleoregions of *species* and *infraspecies* functions by typing:
```python
from pyifpni.pyifpni import IFPNI

ifpni = IFPNI()

ifpni.available_paleoregion()
```
Then you will see:
```base
Available paleoregion list: 
	 ['Africa', 'Africa (East)', 'Africa (Equatorial)', 'Africa (North)', 'Africa (South)', 'Africa (West)', 'Altaida (Altaides)', 'Altaj', 'America', 'America (Caribbean)', 'America (North)', 'America (North - Greenland)', 'America (South)', 'Anatolia', 'Angarida', 'Angarida (Mongolia)', 'Antarctica', 'Arctic', 'Australia', 'Australia (New Zealand)', 'Avalonia', 'Baltica', 'Cathaysia', 'Cathaysia (Kitakamiland)', 'Cathaysia (North)', 'Cathaysia (Sino-Korea)', 'Cathaysia (South)', 'Caucasus', 'China (North)', 'China (South)', 'Chingiz', 'Columbia (Amazonia)', 'Columbia (Australia)', 'Columbia (Baltica)', 'Columbia (East Antarctica)', 'Columbia (Greenland)', 'Columbia (Indostan)', 'Columbia (Kalahari)', 'Columbia (Laurentia)', 'Columbia (North Australia)', 'Columbia (North China)', 'Columbia (South Australia)', 'Columbia (South China)', 'Columbia (West Africa)', 'Columbia (West Australia)', 'Congo-São Francisco (Congo)', 'Eurasia', 'Eurasia (Anatolia)', 'Eurasia (Arabian peninsula)', 'Eurasia (Asia)', 'Eurasia (Asia Minor)', 'Eurasia (Caucasus)', 'Eurasia (Central Asia)', 'Eurasia (Central Asia and Caucasus)', 'Eurasia (Central Asia and Urals)', 'Eurasia (China)', 'Eurasia (Europe)', 'Eurasia (Europe & Urals)', 'Eurasia (Europe and Central Asia)', 'Eurasia (Europe and W Siberia)', 'Eurasia (Far East)', 'Eurasia (Far East & Central Asia)', 'Eurasia (Far East & China)', 'Eurasia (Far East and Japanese Archipelago)', 'Eurasia (Greenland)', 'Eurasia (Himalayas)', 'Eurasia (Indochina)', 'Eurasia (Indostan)', 'Eurasia (Japanese Archipelago)', 'Eurasia (Japanese Archipelago and Sakhalin)', 'Eurasia (Java Island)', 'Eurasia (Maritime Southeast Asia)', 'Eurasia (Mesopotamian Plain)', 'Eurasia (Middle East)', 'Eurasia (Novaja Zemlja Archipelago)', 'Eurasia (S Asia)', 'Eurasia (S Urals)', 'Eurasia (SE Asia)', 'Eurasia (Siberia)', 'Eurasia (Siberia and Central Asia)', 'Eurasia (Siberia and Far East)', 'Eurasia (South China)', 'Eurasia (South East)', 'Eurasia (Tarim Basin)', 'Eurasia (Tibet)', 'Eurasia (Urals)', 'Eurasia (W Asia)', 'Eurasia (W Asia & Caucasus)', 'Eurasia (W Siberia)', 'Eurasia (W Siberia & Central Asia)', 'Europe', 'Europe (Cis-Caspian)', 'Gondwana (Africa)', 'Gondwana (Antarctica)', 'Gondwana (Arabia)', 'Gondwana (Armorica)', 'Gondwana (Australia)', 'Gondwana (Indostan)', 'Gondwana (N Africa)', 'Gondwana (N Africa [Tethys palaeocean])', 'Gondwana (New Caledonia)', 'Gondwana (New Zealand)', 'Gondwana (Perunica)', 'Gondwana (S America)', 'Gondwana (Sardinia)', 'Gondwana (Saxo-Thuringia)', 'Gondwana (South Africa)', 'Gondwana (South America)', 'Kazakhstania', 'Kazakhstania (Xinjiang)', 'Kenorland (Baltica)', 'Kenorland (Kalaharia)', 'Kenorland (Laurentia)', 'Kenorland (Western Australia)', 'Kitakamiland', 'Laurentia', 'Laurussia', 'Laurussia (Anatolia)', 'Laurussia (Armorica)', 'Laurussia (Avalonia)', 'Laurussia (Avalonia & Baltica)', 'Laurussia (Baltica)', 'Laurussia (Cantabria)', 'Laurussia (Iberica)', 'Laurussia (Laurentia)', 'Laurussia (Moesia)', 'Laurussia (Moldanubia)', 'Laurussia (Perunica)', 'Laurussia (Rhenano-Hercynia)', 'Laurussia (Saxo-Thuringia)', 'Moldanubia', 'Mongolia (Western)', 'not specified', 'Pacific', 'Pamir-Alaj', 'Pannotia (Antarctica)', 'Pannotia (Indostan)', 'Pannotia (Siberia)', 'Perunica', 'Proangarida', 'Rodinia', 'Rodinia (Amazonia)', 'Rodinia (Australia)', 'Rodinia (Baltica)', 'Rodinia (Indostan)', 'Rodinia (Laurentia)', 'Rodinia (North China)', 'Rodinia (Rio Plato)', 'Rodinia (Siberia)', 'Rodinia (South China)', 'Siberia', 'Sibumasu', 'Superior Craton (Superior Craton)', 'Tibet', 'Tien Shan', 'Tien Shan (North)', 'Tien Shan (South)', 'Tuva', 'unknown', 'Vaalbara (Kaapvaal)', 'Vaalbara (Pilbara)', 'Xinjiang']
```