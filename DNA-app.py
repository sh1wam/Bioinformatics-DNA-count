import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
        # DNA Nucleotide Count Web App
         
        This app counts the nucleotide composition of query DNA!

         *** 
         """)

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
         ***
         """)

st.header("INTPUT (DNA Query)")
sequence

st.header("OUTPUT (DNA Query)")

# PRINT DICTIONARY
st.subheader("1. Print Dictionary: ")
def DNA_nucleotide_count(seq):
    d = dict([
        ("A", seq.count("A")),
        ("T", seq.count("T")),
        ("G", seq.count("G")),
        ("C", seq.count("C")),
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

# PRINT TEXT
st.subheader("2. Print text: ")
st.write("There are " + str(X["A"]) + " adenine (A) ")
st.write("There are " + str(X["T"]) + " adenine (T) ")
st.write("There are " + str(X["G"]) + " adenine (G) ")
st.write("There are " + str(X["C"]) + " adenine (C) ")


# DISPLAY DATAFRAME
st.subheader("3. Display DataFrame: ")
df = pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0: "count"}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {"index": "nucleotide"})
st.write(df)

# DISPLAY BAR-CHART USING ALTAIR
st.subheader("4. Display Bar-Chart: ")
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)