CREATE DATABASE library_project;

USE library_project;

CREATE TABLE `data_buku` (
  `id_buku` int(10) NOT NULL,
  `judul_buku` char(60) DEFAULT NULL,
  `kategori_buku` char(50) DEFAULT NULL,
  `stock_buku` int NOT NULL
);

INSERT INTO `data_buku` (`id_buku`, `judul_buku`, `kategori_buku`, `stock_buku`) VALUES
(1, 'Python', 'IT', 2),
(2, 'Linguistics and Arts', 'Literatur', 2);


CREATE TABLE `data_user` (
  `id_user` int(11) NOT NULL,
  `nama_user` char(30) DEFAULT NULL,
  `pekerjaan_user` char(15) DEFAULT NULL,
  `email_user` char(60) DEFAULT NULL
);

INSERT INTO data_user VALUES
(1, 'Sheldon Cooper', 'Peneliti', 'sheldon@cooper.com');

SELECT * FROM data_user;

ALTER TABLE `data_user`
  ADD PRIMARY KEY (`id_user`);
  
ALTER TABLE `data_buku`
  ADD PRIMARY KEY (`id_buku`);
  
CREATE TABLE `data_peminjaman` (
  `id_peminjaman` int(11) NOT NULL,
  `idbuku` int(11) DEFAULT NULL,
  `iduser` int(11) DEFAULT NULL,
  `tanggal_peminjaman` date DEFAULT NULL,
  `tanggal_pengembalian` date DEFAULT NULL
);

ALTER TABLE `data_peminjaman`
  ADD PRIMARY KEY (`id_peminjaman`);
  
ALTER TABLE `data_buku`
  MODIFY `id_buku` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
  
ALTER TABLE `data_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
  
ALTER TABLE `data_peminjaman`
  MODIFY `id_peminjaman` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;