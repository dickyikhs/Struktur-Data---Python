{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukkan Tanggal\n",
      "29\n",
      "Masukkan Bulan\n",
      "02\n",
      "Masukkan Tahun\n",
      "2018\n",
      "29  Februari  2018  tidak valid \n"
     ]
    }
   ],
   "source": [
    "class kalender:\n",
    "    print(\"Masukkan Tanggal\")\n",
    "    tanggal= int(input())\n",
    "    print(\"Masukkan Bulan\") \n",
    "    bulan=int(input())\n",
    "    print(\"Masukkan Tahun\")\n",
    "    tahun=int(input())\n",
    "    \n",
    "    if(bulan == 1):\n",
    "        hari = 31\n",
    "        namaBulan = \" Januari \"\n",
    "    elif(bulan == 2):\n",
    "        \n",
    "        if((tahun % 4 == 0 and tahun % 100!=0) or tahun %400 == 0):\n",
    "            hari=29\n",
    "        else:\n",
    "            hari=28\n",
    "        namaBulan = \" Februari \"\n",
    "    \n",
    "    elif(bulan == 3):\n",
    "        hari = 31\n",
    "        namaBulan= \" Maret \"\n",
    "        \n",
    "    elif(bulan == 4):\n",
    "        hari = 30\n",
    "        namaBulan= \" April \"\n",
    "        \n",
    "    elif(bulan == 5):\n",
    "        hari = 31\n",
    "        namaBulan= \" Mei \"\n",
    "        \n",
    "    elif(bulan == 6):\n",
    "        hari = 30\n",
    "        namaBulan= \" Juni \"\n",
    "        \n",
    "    elif(bulan == 7):\n",
    "        hari =31\n",
    "        namaBulan= \" Juli \"\n",
    "        \n",
    "    elif(bulan == 8):\n",
    "        hari = 31\n",
    "        namaBulan= \" Agustus \"\n",
    "        \n",
    "    elif(bulan == 9):\n",
    "        hari = 30\n",
    "        namaBulan= \" September \"\n",
    "        \n",
    "    elif(bulan == 10):\n",
    "        hari = 31\n",
    "        namaBulan= \" Oktober \"\n",
    "        \n",
    "    elif(bulan == 11):\n",
    "        hari = 30\n",
    "        namaBulan= \" November \"\n",
    "        \n",
    "    elif(bulan == 12):\n",
    "        hari = 31\n",
    "        namaBulan= \" Desember \"\n",
    "        \n",
    "    else:\n",
    "        hari = -1\n",
    "        namaBulan= bulan\n",
    "        \n",
    "    bTanggal = tanggal >=1 and tanggal <= hari\n",
    "    bBulan = bulan >=1 and bulan <=12\n",
    "    bValid = bTanggal and bBulan \n",
    "    \n",
    "    \n",
    "    if(bValid):\n",
    "        hasil = \" valid \"\n",
    "    else:\n",
    "        hasil = \" tidak valid \"\n",
    "        \n",
    "    print(\"%d %s %d %s\"%(tanggal,namaBulan,tahun, hasil))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
