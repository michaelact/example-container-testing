# Example Container Testing
Example of Container Testing Tools Implementation

## Tabel Perbandingan
|                 | **Container Structure Test** | **Goss**   | **InSpec**   | **ServerSpec** | **TestInfra** |
|-----------------|------------------------------|------------|--------------|----------------|---------------|
| **Bahasa**      | YAML                         | YAML       | Ruby         | Ruby           | Python        |
| **Komunitas**   | Sedang                       | Sedang     | Luas         | Kecil          | Sedang        |
| **Popularitas** | 2k bintang                   | 5k bintang | 2.6k bintang | 2.5k bintang   | 2.1k bintang  |
| **Biaya**       | Gratis                       | Gratis     | Berbayar     | Gratis         | Gratis        |
| **Kemudahan**   | Sangat Mudah                 | Mudah      | Sedang       | Sedang         | Sedang        |

## Spesifikasi
- **Dukungan komunitas yang kuat**: Mudah untuk mengumpulkan orang-orang yang mengerti tentang kasus dan masalah yang kita hadapi ketika menggunakan alat tersebut.
- **Aktif development**: Alat yang tidak aktif _development_, rawan menjadi gerbang masuk dari serangan keamanan.
- **Mudah untuk dipelajari.**

## Studi kasus
- Memiliki label tertentu
- Dockerfile memiliki instruksi untuk upgrade OS packages
- Sistem operasi yang digunakan bukan Alpine

## Rekomendasi
- Container Structure Test: 
  - Pembuatan rule yang mudah
  - Sedikit syntax yang perlu dipelajari
  - Menggunakan YAML
  - Secara khusus untuk container saja
  - Aktif development
