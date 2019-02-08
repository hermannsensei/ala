from hachoir_parser import createParser
from hachoir_core.cmd_line import unicodeFilename
from hachoir_core.tools import makePrintable
from hachoir_core.i18n import getTerminalCharset
from hachoir_metadata import extractMetadata

filename = '/home/mac/Pictures/damso.mp3'
metadata = extractMetadata(createParser(unicodeFilename(filename), filename))

print("Liste des metadonnees Hachoir pour '"+filename+"'")
for value in metadata:
    if(len(value.values)>0):
        ligne = "  "
        ligne += value.description+" : "
        for v in value.values:
          ligne += v.text
        ligne += " ( Attribut hachoir : "+value.key+" )"
        print(ligne)