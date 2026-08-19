

dna_sequence=input("Enter DNA sequence: ")
def count_bases(dna_sequence):
    A_count=dna_sequence.count("A")
    T_count=dna_sequence.count("T")
    G_count=dna_sequence.count("G")
    C_count=dna_sequence.count("C")
    return A_count,T_count,G_count,C_count
A_count, T_count, G_count, C_count= count_bases(dna_sequence)
total_num_base=(A_count+T_count+G_count+C_count)
gc_content=round(((G_count+C_count)/total_num_base)*100,2)
print(gc_content)
def sequence_type(gc_content):
    if gc_content>=60:
        return "GC-rich"
    else:
        return "AT-rich"
classification = sequence_type(gc_content)
print(f"A:{A_count},T:{T_count},G:{G_count},C:{C_count},Classification:{classification}")





