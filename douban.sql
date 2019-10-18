
sudo docker run --name bookdb -p 3306:3306 -e MYSQL\_ROOT\_PASSWORD=123456 -d mysql


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

mysql> show warnings;
+---------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Level   | Code | Message                                                                                                                                                                     |
+---------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Warning | 1681 | Specifying number of digits for floating point data types is deprecated and will be removed in a future release.                                                            |
| Warning | 1681 | Specifying number of digits for floating point data types is deprecated and will be removed in a future release.                                                            |
| Warning | 3719 | 'utf8' is currently an alias for the character set UTF8MB3, but will be an alias for UTF8MB4 in a future release. Please consider using UTF8MB4 in order to be unambiguous. |
+---------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


book_title,book_douban_id,book_rate,book_author,book_rate_user,book_press,book_press_date,book_price



CREATE USER 'douban'@'127.0.0.1' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON douban_book.* TO 'douban'@'127.0.0.1' WITH GRANT OPTION;



# 插入数据(元组或列表)
effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))
    
# 插入数据(字典)
info = {'name': 'fake', 'age': 15}
effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%(name)s, %(age)s)', info)
    
connection.commit()


cursor = connection.cursor()
    
# 批量插入
effect_row = cursor.executemany(
    'INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', [
        ('hello', 13),
        ('fake', 28),
    ])
    
connection.commit()