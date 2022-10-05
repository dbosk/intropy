import phonebook as pb

phonebook = {
    "adam": "0701234567",
    "bertil": "0721234567"
}
phonebook["david"] = "0741234567"
phonebook["cesar"] = "0731234567"
phonebook.update({
    "kalle": "+3320484737893",
    "erik": "070123456789",
    "filip": "07012345459",
    "helge": "087900000",
    "ivar": "087638393",
    "johan": "20892983928",
    "gustav": "060123456"
})

pb.print_sorted(phonebook)
pb.interactive_search(phonebook)
