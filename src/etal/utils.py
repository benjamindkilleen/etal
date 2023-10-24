import bibtexparser


def process_authors(entry: dict[str, str]):
    authors = entry["author"].split(" and ")
    first_author = authors[0]
    if len(authors) > 1:
        entry["author"] = f"{first_author} and others"
    return entry


def process_file(input_file: str, output_file: str):
    with open(input_file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Process the authors in each entry
    bib_database.entries = [process_authors(entry) for entry in bib_database.entries]

    with open(output_file, "w") as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)


if __name__ == "__main__":
    with open("test.bib") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Process the authors in each entry
    bib_database.entries = [process_authors(entry) for entry in bib_database.entries]

    print(bibtexparser.dumps(bib_database))
