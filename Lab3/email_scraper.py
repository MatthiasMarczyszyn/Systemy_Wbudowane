import re


def email_scraper(file_name: str) -> dict:
    """A simple function that use regex to find all headers of email file

    Parameters
    ----------
    file_name : str
        Name of email file

    Returns
    -------
    dict
        A header grouped in dictionary
    """
    scraped_header = {}
    with open(file_name) as f:
        file_content = f.read()
        email_patern = re.compile(r"((?!Content)(?!Type)[A-Z].*)([:]\s)(.*)")
        email_matches = email_patern.finditer(file_content)

        for matches in email_matches:
            scraped_header[matches.group(1)] = matches.group(3)
    return scraped_header


dic = (email_scraper("example.eml"))
for key in dic:
    print(f"{key} = {dic[key]}")
