## Group Exercise 04 - A big Dictionary

# Write a program that creates a nested dictionary that has a biological or biochemical background
# Each sub-dictionary should contain at least seven different entries
# At least one number and one list
# The Main dictionary should contain at least 8 to 10 different entries
# Let the user either display, manipulate or add an entry to your main dictionary
# All changes have to be viable and be seen by the user
import json

Proteins = {}
Proteins["PRDM1"] = {"Name":"PR domain zinc finger protein 1",
                    "Length":825,
                    "Molecular function":["DNA-binding", "Methyltransferase", "Repressor", "Transferase"],
                    "Biological process":["Adaptive immunity", "Immunity", "Innate immunity", "Transcription", "Transcription regulation"],
                    "Ligand":["Metal-binding", "S-adenosyl-L-methionine", "Zinc"],
                    "Location": "Chromosome 6",
                    "Subcellular location":["Nucleus", "Cytoplasm"],
                    "Sequence":"MLDICLEKRVGTTLAAPKCNSSTVRFQGLAEGTKGTMKMDMEDADMTLWTEAEFEEKCTYIVNDHPWDSGADGGTSVQAEASLPRNLLFKYATNSEEVIGVMSKEYIPKGTRFGPLIGEIYTNDTVPKNANRKYFWRIYSRGELHHFIDGFNEEKSNWMRYVNPAHSPREQNLAACQNGMNIYFYTIKPIPANQELLVWYCRDFAERLHYPYPGELTMMNLTQTQSSLKQPSTEKNELCPKNVPKREYSVKEILKLDSNPSKGKDLYRSNISPLTSEKDLDDFRRRGSPEMPFYPRVVYPIRAPLPEDFLKASLAYGIERPTYITRSPIPSSTTPSPSARSSPDQSLKSSSPHSSPGNTVSPVGPGSQEHRDSYAYLNASYGTEGLGSYPGYAPLPHLPPAFIPSYNAHYPKFLLPPYGMNCNGLSAVSSMNGINNFGLFPRLCPVYSNLLGGGSLPHPMLNPTSLPSSLPSDGARRLLQPEHPREVLVPAPHSAFSFTGAAASMKDKACSPTSGSPTAGTAATAEHVVQPKATSAAMAAPSSDEAMNLIKNKRNMTGYKTLPYPLKKQNGKIKYECNVCAKTFGQLSNLKVHLRVHSGERPFKCQTCNKGFTQLAHLQKHYLVHTGEKPHECQVCHKRFSSTSNLKTHLRLHSGEKPYQCKVCPAKFTQFVHLKLHKRLHTRERPHKCSQCHKNYIHLCSLKVHLKGNCAAAPAPGLPLEDLTRINEEIEKFDISDNADRLEDVEDDISVISVVEKEILAVVRKEKEETGLKVSLQRNMGNGLLSSGCSLYESSDLPLMKLPPSNPLPLVPVKVKQETVEPMDP"}
Proteins["IRF1"] = {"Name":"Interferon regulatory factor 1",
                    "Length":325,
                    "Molecular function":["Activator", "DNA-binding", "Repressor"],
                    "Biological process":["Antiviral defense", "Immunity", "Innate Immunity", "Transcription", "Transcription regulation"],
                    "Location":"Chromosome 5",
                    "Subcellular location":["Nucleus", "Cytoplasm"],
                    "Sequence":"MPITRMRMRPWLEMQINSNQIPGLIWINKEEMIFQIPWKHAAKHGWDINKDACLFRSWAIHTGRYKAGEKEPDPKTWKANFRCAMNSLPDIEEVKDQSRNKGSSAVRVYRMLPPLTKNQRKERKSKSSRDAKSKAKRKSCGDSSPDTFSDGLSSSTLPDDHSSYTVPGYMQDLEVEQALTPALSPCAVSSTLPDWHIPVEVVPDSTSDLYNFQVSPMPSTSEATTDEDEEGKLPEDIMKLLEQSEWQPTNVDGKGYLLNEPGVQPTSVYGDFSCKEEPEIDSPGGDIGLSLQRVFTDLKNMDATWLDSLLTPVRLPSIQAIPCAP"}
Proteins["STAT1"] = {"Name":"Signal transducer and activator of transcription 1",
                    "Length":750,
                    "Molecular function":["Activator", "DNA-binding"],
                    "Biological process":["Antiviral defense", "Host-virus interaction", "Transcription", "Transcription regulation"],
                    "Location":"Chromosome 2",
                    "Subcellular location":["Cytoplasm", "Nucleus"],
                    "Sequence":"MSQWYELQQLDSKFLEQVHQLYDDSFPMEIRQYLAQWLEKQDWEHAANDVSFATIRFHDLLSQLDDQYSRFSLENNFLLQHNIRKSKRNLQDNFQEDPIQMSMIIYSCLKEERKILENAQRFNQAQSGNIQSTVMLDKQKELDSKVRNVKDKVMCIEHEIKSLEDLQDEYDFKCKTLQNREHETNGVAKSDQKQEQLLLKKMYLMLDNKRKEVVHKIIELLNVTELTQNALINDELVEWKRRQQSACIGGPPNACLDQLQNWFTIVAESLQQVRQQLKKLEELEQKYTYEHDPITKNKQVLWDRTFSLFQQLIQSSFVVERQPCMPTHPQRPLVLKTGVQFTVKLRLLVKLQELNYNLKVKVLFDKDVNERNTVKGFRKFNILGTHTKVMNMEESTNGSLAAEFRHLQLKEQKNAGTRTNEGPLIVTEELHSLSFETQLCQPGLVIDLETTSLPVVVISNVSQLPSGWASILWYNMLVAEPRNLSFFLTPPCARWAQLSEVLSWQFSSVTKRGLNVDQLNMLGEKLLGPNASPDGLIPWTRFCKENINDKNFPFWLWIESILELIKKHLLPLWNDGCIMGFISKERERALLKDQQPGTFLLRFSESSREGAITFTWVERSQNGGEPDFHAVEPYTKKELSAVTFPDIIRNYKVMAAENIPENPLKYLYPNIDKDHAFGKYYSRPKEAPEPMELDGPKGTGYIKTELISVSEVHPSRLQTTDNLLPMSPEEFDEVSRIVGSVEFDSMMNTV"}
Proteins["MCM5"] = {"Name":"Minichromosome maintenance complex component 5",
                    "Length":734,
                    "Molecular function":["DNA-binding", "Helicase", "Hydrolase"],
                    "Biological process":["Cell cycle", "DNA replication"],
                    "Ligand":["ATP-binding", "Nucleotide-binding"],
                    "Location": "Chromosome 22",
                    "Subcellular location":["Nucleus", "Chromosome"],
                    "Sequence":"MSGFDDPGIFYSDSFGGDAQADEGQARKSQLQRRFKEFLRQYRVGTDRTGFTFKYRDELKRHYNLGEYWIEVEMEDLASFDEDLADYLYKQPAEHLQLLEEAAKEVADEVTRPRPSGEEVLQDIQVMLKSDASPSSIRSLKSDMMSHLVKIPGIIIAASAVRAKATRISIQCRSCRNTLTNIAMRPGLEGYALPRKCNTDQAGRPKCPLDPYFIMPDKCKCVDFQTLKLQELPDAVPHGEMPRHMQLYCDRYLCDKVVPGNRVTIMGIYSIKKFGLTTSRGRDRVGVGIRSSYIRVLGIQVDTDGSGRSFAGAVSPQEEEEFRRLAALPNVYEVISKSIAPSIFGGTDMKKAIACLLFGGSRKRLPDGLTRRGDINLLMLGDPGTAKSQLLKFVEKCSPIGVYTSGKGSSAAGLTASVMRDPSSRNFIMEGGAMVLADGGVVCIDEFDKMREDDRVAIHEAMEQQTISIAKAGITTTLNSRCSVLAAANSVFGRWDETKGEDNIDFMPTILSRFDMIFIVKDEHNEERDVMLAKHVITLHVSALTQTQAVEGEIDLAKLKKFIAYCRVKCGPRLSAEAAEKLKNRYIIMRSGARQHERDSDRRSSIPITVRQLEAIVRIAEALSKMKLQPFATEADVEEALRLFQVSTLDAALSGTLSGVEGFTSQEDQEMLSRIEKQLKRRFAIGSQVSEHSIIKDFTKQKYPEHAIHKVLQLMLRRGEIQHRMQRKVLYRLK"}
Proteins["ORC2"] = {"Name":"Origin recognition complex subunit 2",
                    "Length":577,
                    "Biological process":["DNA replication"],
                    "Location":"Chromosome 2",
                    "Subcellular location":["Nucleus"],
                    "Sequence":"MSKPELKEDKMLEVHFVGDDDVLNHILDREGGAKLKKERAQLLVNPKKIIKKPEYDLEEDDQEVLKDQNYVEIMGRDVQESLKNGSATGGGNKVYSFQNRKHSEKMAKLASELAKTPQKSVSFSLKNDPEITINVPQSSKGHSASDKVQPKNNDKSEFLSTAPRSLRKRLIVPRSHSDSESEYSASNSEDDEGVAQEHEEDTNAVIFSQKIQAQNRVVSAPVGKETPSKRMKRDKTSDLVEEYFEAHSSSKVLTSDRTLQKLKRAKLDQQTLRNLLSKVSPSFSAELKQLNQQYEKLFHKWMLQLHLGFNIVLYGLGSKRDLLERFRTTMLQDSIHVVINGFFPGISVKSVLNSITEEVLDHMGTFRSILDQLDWIVNKFKEDSSLELFLLIHNLDSQMLRGEKSQQIIGQLSSLHNIYLIASIDHLNAPLMWDHAKQSLFNWLWYETTTYSPYTEETSYENSLLVKQSGSLPLSSLTHVLRSLTPNARGIFRLLIKYQLDNQDNPSYIGLSFQDFYQQCREAFLVNSDLTLRAQLTEFRDHKLIRTKKGTDGVEYLLIPVDNGTLTDFLEKEEEEA"}
Proteins["CDC6"] = {"Name":"Cell division control protein 6 homolog",
                    "Length":560,
                    "Biological process":["Cell cycle", "Cell division", "DNA replication", "Mitosis"],
                    "Ligand":["ATP-binding", "Nucleotide-binding"],
                    "Location":"Chromosome 17",
                    "Subcellular location":["Nucleus", "Cytoplasm"],
                    "Sequence":"MPQTRSQAQATISFPKRKLSRALNKAKNSSDAKLEPTNVQTVTCSPRVKALPLSPRKRLGDDNLCNTPHLPPCSPPKQGKKENGPPHSHTLKGRRLVFDNQLTIKSPSKRELAKVHQNKILSSVRKSQEITTNSEQRCPLKKESACVRLFKQEGTCYQQAKLVLNTAVPDRLPAREREMDVIRNFLREHICGKKAGSLYLSGAPGTGKTACLSRILQDLKKELKGFKTIMLNCMSLRTAQAVFPAIAQEICQEEVSRPAGKDMMRKLEKHMTAEKGPMIVLVLDEMDQLDSKGQDVLYTLFEWPWLSNSHLVLIGIANTLDLTDRILPRLQAREKCKPQLLNFPPYTRNQIVTILQDRLNQVSRDQVLDNAAVQFCARKVSAVSGDVRKALDVCRRAIEIVESDVKSQTILKPLSECKSPSEPLIPKRVGLIHISQVISEVDGNRMTLSQEGAQDSFPLQQKILVCSLMLLIRQLKIKEVTLGKLYEAYSKVCRKQQVAAVDQSECLSLSGLLEARGILGLKRNKETRLTKVFFKIEEKEIEHALKDKALIGNILATGLP"}
Proteins["KPSH1"] = {"Name":"Serine/threonine-protein kinase H1",
                    "Length":424,
                    "Molecular function":["Kinase", "Serine/threonine-protein kinase", "Transferase"],
                    "Ligand":["ATP-binding", "Nucleotide-binding"],
                    "Location":"Chromosome 16",
                    "Subcellular location":["Golgi apparatus", "Cytoplasm", "Nucleus", "Endoplasmic reticulum"],
                    "Sequence":"MGCGTSKVLPEPPKDVQLDLVKKVEPFSGTKSDVYKHFITEVDSVGPVKAGFPAASQYAHPCPGPPTAGHTEPPSEPPRRARVAKYRAKFDPRVTAKYDIKALIGRGSFSRVVRVEHRATRQPYAIKMIETKYREGREVCESELRVLRRVRHANIIQLVEVFETQERVYMVMELATGGELFDRIIAKGSFTERDATRVLQMVLDGVRYLHALGITHRDLKPENLLYYHPGTDSKIIITDFGLASARKKGDDCLMKTTCGTPEYIAPEVLVRKPYTNSVDMWALGVIAYILLSGTMPFEDDNRTRLYRQILRGKYSYSGEPWPSVSNLAKDFIDRLLTVDPGARMTALQALRHPWVVSMAASSSMKNLHRSISQNLLKRASSRCQSTKSAQSTRSSRSTRSNKSRRVRERELRELNLRYQQQYNG"}
Proteins["MAPK2"] = {"Name":"Mitogen-activated protein kinase 2",
                    "Length":400,
                    "Molecular function":["Kinase", "Serin/threonine-protein kinase", "Transferase"],
                    "Biological process":["DNA damage"],
                    "Ligand":["ATP-binding", "Nucleotide-binding"],
                    "Location":"Chromosome 1",
                    "Subcellular location":["Cytoplasm, Nucleus"],
                    "Sequence":"MLSNSQGQSPPVPFPAPAPPPQPPTPALPHPPAQPPPPPPQQFPQFHVKSGLQIKKNAIIDDYKVTSQVLGLGINGKVLQIFNKRTQEKFALKMLQDCPKARREVELHWRASQCPHIVRIVDVYENLYAGRKCLLIVMECLDGGELFSRIQDRGDQAFTEREASEIMKSIGEAIQYLHSINIAHRDVKPENLLYTSKRPNAILKLTDFGFAKETTSHNSLTTPCYTPYYVAPEVLGPEKYDKSCDMWSLGVIMYILLCGYPPFYSNHGLAISPGMKTRIRMGQYEFPNPEWSEVSEEVKMLIRNLLKTEPTQRMTITEFMNHPWIMQSTKVPQTPLHTSRVLKEDKERWEDVKEEMTSALATMRVDYEQIKIKKIEDASNPLLLKRRKKARALEAAALAH"}


print("Here is the Protein dictionary:")
tmp = json.dumps(Proteins, indent=4)
print(tmp)

user_op = input("\nWhat action would you like to perform for the dictionary? \nChoose either search, add, delete or change.\n")
# Adding to the dictionary. Either a whole new protein or add a new key-value pair to an existing protein
if user_op == "add":
    user_input = input("Do you want to add a whole new protein (new) or add information to an existing protein (add)?\n")
    if user_input == "new":
        print("Please provide the information of the protein you want to add.")
        prot_abbr = input("Abbreviation: ")
        if prot_abbr in Proteins:
            print(f"{prot_abbr} already exists in the dictionary! It will not be added to avoid errors.")
        else:
            prot_name = input("Full name: ")
            prot_length = int(input("Length (Amino acids): "))
            prot_molfunction = input("Molecular function: ").split()
            prot_biolprocess = input("Biological process: ").split()
            prot_ligand = input("Ligands: ").split()
            prot_location = input("Location (Chromosome): ")
            prot_subcell = input("Subcellular location: ").split()
            prot_sequence = input("Sequence: ")
            Proteins[prot_abbr] = {"Name":prot_name,
                                    "Length":prot_length,
                                    "Molecular function":prot_molfunction,
                                    "Biological process":prot_biolprocess,
                                    "Ligand":prot_ligand,
                                    "Location":prot_location,
                                    "Subcellular location":prot_subcell,
                                    "Sequence":prot_sequence}


            tmp = json.dumps(Proteins, indent=4)
            print(f"This is the new dictionary: \n{tmp}")
    elif user_input == "add":
        print("Please provide the information you want to add.")
        prot_abbr = input("Abbreviation: ")
        if prot_abbr in Proteins:
            prot_key = input("Key: ")
            prot_value = input("Value: ")
            if prot_value.isdigit():
                prot_value = int(prot_value)
            Proteins[prot_abbr][prot_key] = prot_value

            tmp = json.dumps(Proteins[prot_abbr], indent=4)
            print(f"Here is the entry for {prot_abbr}: \n{tmp}")
        else:
            print(f"{prot_abbr} was not found in the dictionary!")
    else:
        print("Invalid Input")
# Deleting an entry. Asks the user for the abbreviation of the protein, which should be deleted.
elif user_op == "delete":
    prot_abbr= input("Which protein do you want to delete? \nAbbreviation: ")
    if prot_abbr in Proteins:
        del Proteins[prot_abbr]

        tmp = json.dumps(Proteins, indent=4)
        print(f"This is the new dictionary: \n{tmp}")
    else:
        print(f"{prot_abbr} was not found in the dictionary!")
# Changing entries. Can only change values and not keys.
elif user_op == "change":
    prot_abbr = input("Of which protein do you want to change the information?\nAbbreviation: ")
    if prot_abbr in Proteins:
        print("Choose from the following list, which part you want to change:")
        # prints a changing list depending on the existing keys
        print(*list(Proteins[prot_abbr].keys()), sep=', ')
        prot_key = input()
        if prot_key in list(Proteins[prot_abbr].keys()):
            prot_value = input("New information:")
            if prot_value.isdigit():
                prot_value = int(prot_value)
            Proteins[prot_abbr][prot_key] = prot_value

            tmp = json.dumps(Proteins, indent=4)
            print(f"This is the new dictionary: \n{tmp}")
        else:
            print(f"{prot_key} is no available key in {prot_abbr}.")
    else:
        print(f"{prot_abbr} was not found in the dictionary!")
# Search for a protein
elif user_op == "search":
    prot_abbr = input("Which protein are you looking for? \nAbbreviation: ")
    if prot_abbr in Proteins:
        tmp = json.dumps(Proteins[prot_abbr], indent=4)
        print(f"Here is the entry for {prot_abbr}: \n{tmp}")
    else:
        print(f"{prot_abbr} was not found in the dictionary!")
# Invalid input if none of the above are true
else:
    print("Invalid Input")
