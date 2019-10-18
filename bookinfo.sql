CREATE TABLE IF NOT EXISTS `bookinfo`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `book_title` VARCHAR(100) NOT NULL,
   `book_douban_id` INT UNSIGNED NOT NULL,
   `book_rate` FLOAT(3,2) NOT NULL,
   `book_author` VARCHAR(100) NOT NULL,
   `book_rate_user` INT UNSIGNED NOT NULL,
   `book_press` VARCHAR(100) NOT NULL,
   `book_press_date` DATE,
   `book_price` FLOAT(6,2) NOT NULL,
   `book_tag` VARCHAR(100) NOT NULL,
   `createtime` DATE DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
