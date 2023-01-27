import streamlit as st

if "isimler" not in st.session_state:
    st.session_state.isimler=[]
if "tcknler" not in st.session_state:
    st.session_state.tcknler=[]
if "yaslar" not in st.session_state:
    st.session_state.yaslar=[]

isimlist=st.session_state.isimler
tcknlist=st.session_state.tcknler
yaslist=st.session_state.yaslar

isim=st.text_input("İsminizi giriniz")
tckn=st.number_input("TCKN giriniz",step=1)
yas=st.text_input("Yaşınızı giriniz")
if st.button("Kayıt Ol") :
    if len(str(tckn)) == 11:
        if tckn in tcknlist:
            st.write("Kullanıcı zaten var")
        else:
            isimlist.append(isim)
            tcknlist.append(tckn)
            yaslist.append(yas)
    else:
        st.write("Geçerli TCKN Giriniz")

st.write(isimlist)
st.write(tcknlist)
st.write(yaslist)

siltckn=st.number_input("Sİlmek sitediğiniz kişinin tcknsini girin",step=1)
if st.button("Kayıt sil"):
    if len(str(siltckn)) == 11:
        if siltckn in tcknlist:
            st.write("Kayıt silindi")
            indexsayi = tcknlist.index(siltckn)
            isimlist.pop(indexsayi)
            tcknlist.pop(indexsayi)
            yaslist.pop(indexsayi)
        else:
            st.write("Böyle bir kullanıcı yok")
            indexsayi=tcknlist.index(siltckn)

if st.button("Geçersiz TCKN'leri temizle"):
    for a in tcknlist:
        st.write(str(a)[-1])
        if int(str(a)[-1]) % 2 != 0 :
            sayiindex=tcknlist.index(a)
            isimlist.pop(sayiindex)
            tcknlist.pop(sayiindex)
            yaslist.pop(sayiindex)

st.write(isimlist)
st.write(tcknlist)
st.write(yaslist)

