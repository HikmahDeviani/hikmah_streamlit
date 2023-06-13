import streamlit as st
import pandas as pd
import streamlit as st
import numpy as np

# Judul halaman
st.title("Kalkulator Matriks")

# Input dimensi matriks
st.subheader("Input Dimensi Matriks")
rows_A = st.number_input("Baris matriks A", min_value=1, value=1, step=1)
cols_A = st.number_input("Kolom matriks A", min_value=1, value=1, step=1)
rows_B = st.number_input("Baris matriks B", min_value=1, value=1, step=1)
cols_B = st.number_input("Kolom matriks B", min_value=1, value=1, step=1)

# Input elemen-elemen matriks
st.subheader("Input Elemen-elemen Matriks")
matrix_A = []
matrix_B = []

for i in range(rows_A):
    row = []
    for j in range(cols_A):
        element = st.number_input(f"Elemen A[{i}][{j}]", value=0.0)
        row.append(element)
    matrix_A.append(row)

for i in range(rows_B):
    row = []
    for j in range(cols_B):
        element = st.number_input(f"Elemen B[{i}][{j}]", value=0.0)
        row.append(element)
    matrix_B.append(row)

# Operasi matriks
st.subheader("Operasi Matriks")
operation = st.selectbox("Pilih operasi matriks", ("Penjumlahan", "Pengurangan", "Perkalian"))

if operation == "Penjumlahan":
    result = np.add(matrix_A, matrix_B)
elif operation == "Pengurangan":
    result = np.subtract(matrix_A, matrix_B)
elif operation == "Perkalian":
    try:
        result = np.dot(matrix_A, matrix_B)
    except ValueError:
        st.error("Jumlah kolom matriks A harus sama dengan jumlah baris matriks B untuk melakukan perkalian.")

# Menampilkan hasil operasi
if "result" in locals():
    st.subheader("Hasil Operasi")
    st.write(np.array(result))
