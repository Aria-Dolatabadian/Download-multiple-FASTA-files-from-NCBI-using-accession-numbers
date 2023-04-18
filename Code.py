from Bio import SeqIO
from Bio import Entrez

# Set your email address to identify yourself to NCBI
Entrez.email = "your.email@example.com"

# Set the list of GenBank IDs for the records you want to download
genbank_ids = ["MK576039.1", "MK672908.1", "MK672907.1","MK672906.1","KT072939.1","KT072928.1","KT072903.1","MF092945.1","MF092943.1","JQ003574.1",
"JQ003570.1","JQ003569.1","EU090046.1","EU090045.1","EU090044.1","EU090043.1","EU090042.1","EU090041.1","EU090040.1","EU090039.1",
"EU090038.1","EU090037.1","EU090036.1","DQ222440.1","JN162783.1","JN162782.1","JN162781.1","KC969742.1","KC969741.1","KF959650.1",
"KF959647.1","KF959640.1","JX905660.1","KC736594.1","HQ828194.2","HQ828187.2","HQ912452.1","HQ912451.1","AB430676.1","AM713181.1","AM710473.1"]

# Use the Entrez.efetch function to download the records in FASTA format
handle = Entrez.efetch(db="nucleotide", id=genbank_ids, rettype="fasta")

# Parse the downloaded records with SeqIO.parse and save them to a file
with open("Fragilaria sequences.fasta", "w") as output:
    records = SeqIO.parse(handle, "fasta")
    SeqIO.write(records, output, "fasta")
