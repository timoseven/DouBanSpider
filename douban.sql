
sudo docker run --name bookdb -p 3306:3306 -e MYSQL\_ROOT\_PASSWORD=123456 -d mysql


CREATE TABLE IF NOT EXISTS `bookinfo`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `book_title` VARCHAR(100) NOT NULL,
   `book_douban_id` INT UNSIGNED NOT NULL,
   `book_rate` FLOAT(3,2) NOT NULL,
   `book_author` VARCHAR(100) NOT NULL,
   `book_rate_user` INT UNSIGNED NOT NULL,
   `book_press` VARCHAR(100) NOT NULL,
   `book_press_date` VARCHAR(20) NOT NULL,
   `book_price` FLOAT(6,2) NOT NULL,
   `book_tag` VARCHAR(100) NOT NULL,
   `createtime` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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
GRANT ALL PRIVILEGES ON douban_book.* TO 'douban'@'127.0.0.1'IDENTIFIED BY '123456';



# 插入数据(元组或列表)
effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))
    


Traceback (most recent call last):
  File "doubanSpider.py", line 220, in <module>
    do_spider(book_tag_lists)
  File "doubanSpider.py", line 168, in do_spider
    'INSERT INTO bookinfo (book_title, book_douban_id,book_rate,book_author,book_rate_user,book_press,book_press_date,book_price,book_tag) VALUES ("%s", %d, %f, "%s", %d, "%s", "%s", %f, "%s")', (book_list[0],))
  File "/Users/timo/.pyenv/versions/venv369/lib/python3.6/site-packages/pymysql/cursors.py", line 199, in executemany
    self.rowcount = sum(self.execute(query, arg) for arg in args)
  File "/Users/timo/.pyenv/versions/venv369/lib/python3.6/site-packages/pymysql/cursors.py", line 199, in <genexpr>
    self.rowcount = sum(self.execute(query, arg) for arg in args)
  File "/Users/timo/.pyenv/versions/venv369/lib/python3.6/site-packages/pymysql/cursors.py", line 168, in execute
    query = self.mogrify(query, args)
  File "/Users/timo/.pyenv/versions/venv369/lib/python3.6/site-packages/pymysql/cursors.py", line 147, in mogrify
    query = query % self._escape_args(args, conn)
TypeError: %d format: a number is required, not str


https://blog.csdn.net/jy1690229913/article/details/79407224
在写sql语句时，不管字段为什么类型，占位符统一使用%s,且不能加上引号


https://github.com/PyMySQL/PyMySQL/blob/master/pymysql/converters.py