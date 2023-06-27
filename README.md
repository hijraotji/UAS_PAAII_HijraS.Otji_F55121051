# UAS_PAAII_HijraS.Otji_F55121051
Program Bubble Sort dan Insertion Sort:

Analisis Bubble Sort:
Algoritma: Bubble Sort membandingkan elemen-elemen bersebelahan dalam daftar dan menukar mereka jika urutannya tidak benar. Ini mengulangi proses ini sampai daftar benar-benar terurut.
Kompleksitas Waktu:
Kasus Terburuk: O(n^2)
Kasus Terbaik: O(n)
Kasus Rata-rata: O(n^2)
Analisis:
Bubble Sort lebih cocok digunakan untuk daftar yang sangat kecil atau hampir terurut. Karena kompleksitas waktunya yang tinggi dalam kasus terburuk, Bubble Sort tidak efisien untuk daftar yang besar.
Dalam kasus terbaik, jika daftar sudah terurut, Bubble Sort memiliki kinerja yang baik karena hanya membutuhkan satu iterasi untuk memverifikasi bahwa daftar sudah terurut.

Analisis Insertion Sort:
Algoritma: Insertion Sort membagi daftar menjadi dua bagian, bagian terurut dan bagian yang belum terurut. Pada setiap iterasi, elemen dari bagian belum terurut dipindahkan ke posisi yang tepat dalam bagian terurut dengan membandingkannya dengan elemen sebelumnya.
Kompleksitas Waktu:
Kasus Terburuk: O(n^2)
Kasus Terbaik: O(n)
Kasus Rata-rata: O(n^2)
Analisis:
Insertion Sort juga lebih cocok untuk daftar yang kecil atau hampir terurut. Dalam kasus terburuk, kompleksitas waktu Insertion Sort sama dengan Bubble Sort. Namun, dalam kasus terbaik, Insertion Sort memiliki kinerja yang lebih baik karena hanya membutuhkan satu iterasi untuk memverifikasi bahwa daftar sudah terurut.

Program TSP dan Dijkstra:
Analisis TSP:
Algoritma: TSP menggunakan pendekatan heuristik yang sederhana untuk mencari jalur terpendek yang mengunjungi setiap simpul tepat satu kali dan kembali ke simpul awal.
Kompleksitas Waktu:
Kasus Terburuk: O(n^2)
Kasus Terbaik: O(n-1)
Kasus Rata-rata: O(n^2)
Analisis:
Algoritma TSP yang digunakan dalam program ini adalah pendekatan heuristik yang tidak menjamin solusi optimal. Kompleksitas waktunya bervariasi tergantung pada jumlah simpul dalam graf. Untuk jumlah simpul yang besar, algoritma TSP yang lebih efisien seperti Algoritma Penurunan atau Algoritma Genetika lebih disarankan.

Analisis Dijkstra:
Algoritma: Dijkstra digunakan untuk mencari jalur terpendek antara dua simpul dalam graf dengan bobot tak negatif. Ini memperbarui jarak terpendek ke setiap simpul seiring berjalannya.
Kompleksitas Waktu: O((|V| + |E|) log |V|), di mana |V| adalah jumlah simpul dan |E| adalah jumlah tepi dalam graf.
Analisis:
Algoritma Dijkstra memberikan solusi optimal dalam mencari jalur terpendek dalam graf dengan bobot tak negatif. Namun, kompleksitas waktunya lebih tinggi dibandingkan dengan beberapa algoritma lain seperti Breadth-First Search (BFS) jika graf tidak memiliki bobot atau memiliki bobot yang sama untuk setiap tepi.
Dalam kasus terbaik, Dijkstra memiliki kinerja yang sama dengan BFS, yaitu O(|V| + |E|).
Algoritma ini cocok digunakan untuk graf dengan jumlah simpul dan tepi yang moderat.
