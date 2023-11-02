# fasta_replace_pipes.py
# How_to_use=python fasta_replace_pipes.py Thielaviopsis_euricoi.fasta Thielaviopsis_euricoi_modified.fasta
def replace_pipes_in_fasta(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):  # Header line
                outfile.write(line.replace('|', '_'))
            else:
                outfile.write(line)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python fasta_replace_pipes.py input.fasta output.fasta")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    replace_pipes_in_fasta(input_path, output_path)
    print(f"Modified file saved to {output_path}")

