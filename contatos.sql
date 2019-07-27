use agenda;
CREATE TABLE IF NOT EXISTS `contatos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
  `telefone` varchar(13) NOT NULL,
  `celular` varchar(14) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`telefone`),
  UNIQUE (`celular`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
insert into contatos (nome, telefone, celular) values ('matheus', '(84)8890-7891', '(84)98890-7891');
