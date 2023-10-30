# Data-Scraper [WIP]
> A data-scraper that makes it possible to filter out the most important information from huge amounts of text based data.

The script asks for a ***keyword*** to search for. It compares the keyword with the ***file-name*** and its ***contents***. As soon as it finds the keyword in it, it is listed as a match and output at the end.  
## File Content Read
> The scraper is able to read only the following text-based files:
- .docx
- .pdf
- .txt
## Usage
The scraper is searching the `./DATA` **directory** by default. To change that you have to edit the **variable** `directory`.

_Line 9_: `directory = "./DATA"`
> [!NOTE]
> It iterates through every file in the directory. To speed up the process, it is recommended to limit the amount of files.
## Requirements
> How to install the required libraries.
```
pip install pdfplumber
```
```
pip install docx
```

## Improving
Suggestions for improvements are welcome.
