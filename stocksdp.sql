create database stockdp;
use stockdp;

create table stock_tab(sid integer primary key auto_increment,pname varchar(30),
qty integer(10),rate float(20),manu varchar(30),cata varchar(30));

insert into stock_tab (pname, qty, rate, manu, cata) values
('T-shirt', 50, 12.99, 'ABC', 'Apparel'),
('Sneakers', 100, 49.99, 'XYZ', 'Footwear'),
('Backpack', 75, 29.99, 'PackCo', 'Accessories'),
('Smartphone', 200, 699.99, 'TechCorp', 'Electronics'),
('Headphones', 30, 89.99, 'AudioInc', 'Electronics'),
('Jeans', 50, 39.99, 'DenimCo', 'Apparel'),
('Watch', 40, 199.99, 'TimeCo', 'Accessories'),
('Laptop', 25, 1199.99, 'TechCorp', 'Electronics'),
('Dress', 20, 79.99, 'FashionX', 'Apparel'),
('Sunglasses', 15, 129.99, 'EyewearInc', 'Accessories'),
('Running Shoes', 30, 79.99, 'RunnersCo', 'Footwear'),
('Dumbbell Set', 10, 49.99, 'FitEquip', 'Fitness'),
('Skirt', 25, 29.99, 'FashionX', 'Apparel'),
('Wireless Mouse', 40, 19.99, 'TechCorp', 'Electronics'),
('Guitar', 20, 299.99, 'MusicWorks', 'Instruments'),
('Hoodie', 35, 24.99, 'CozyWear', 'Apparel'),
('Yoga Mat', 30, 19.99, 'FitEquip', 'Fitness'),
('Eyeliner', 50, 9.99, 'BeautyCo', 'Cosmetics'),
('Keyboard', 15, 49.99, 'TechCorp', 'Electronics'),
('Wristwatch', 25, 149.99, 'TimeCo', 'Accessories'),
('Running Shorts', 30, 19.99, 'RunnersCo', 'Apparel'),
('Bluetooth Speaker', 40, 79.99, 'AudioInc', 'Electronics'),
('Tennis Racket', 20, 99.99, 'SportsCo', 'Sports'),
('Perfume', 30, 59.99, 'FragranceX', 'Beauty'),
('Dress Shoes', 25, 59.99, 'FootwearCo', 'Footwear'),
('Wireless Earbuds', 35, 129.99, 'AudioInc', 'Electronics'),
('Cookware Set', 10, 149.99, 'KitchenX', 'Kitchen'),
('Hair Dryer', 20, 39.99, 'BeautyCo', 'Appliances'),
('Running Jacket', 15, 49.99, 'RunnersCo', 'Apparel'),
('Desktop Computer', 10, 999.99, 'TechCorp', 'Electronics'),
('Leather Wallet', 25, 39.99, 'LeatherWorks', 'Accessories'),
('Cologne', 30, 69.99, 'FragranceX', 'Beauty'),
('Tennis Shoes', 40, 69.99, 'SportsCo', 'Footwear'),
('Wireless Keyboard', 20, 59.99, 'TechCorp', 'Electronics'),
('Yoga Pants', 25, 29.99, 'FitEquip', 'Fitness'),
('Eyeshadow Palette', 15, 19.99, 'BeautyCo', 'Cosmetics'),
('Digital Camera', 20, 399.99, 'PhotographyInc', 'Electronics'),
('Chef\'s Knife', 30, 39.99, 'KitchenX', 'Kitchen'),
('Sweater', 40, 34.99, 'CozyWear', 'Apparel'),
('Soccer Ball', 25, 19.99, 'SportsCo', 'Sports'),
('Foundation', 20, 29.99, 'BeautyCo', 'Cosmetics'),
('Jump Rope', 30, 9.99, 'FitEquip', 'Fitness'),
('Office Chair', 15, 99.99, 'OfficeFurn', 'Furniture'),
('Lipstick', 25, 14.99, 'BeautyCo', 'Cosmetics'),
('Tennis Skirt', 10, 24.99, 'SportsCo', 'Apparel'),
('Fitness Tracker', 20, 79.99, 'FitEquip', 'Fitness'),
('Rolling Backpack', 25, 49.99, 'PackCo', 'Accessories'),
('Digital Scale', 15, 29.99, 'KitchenX', 'Kitchen'),
('Ankle Socks', 40, 9.99, 'SockCo', 'Apparel'),
('Water Bottle', 30, 14.99, 'HydrateInc', 'Accessories'),
('Cleanser', 25, 19.99, 'BeautyCo', 'Skincare'),
('Pencil Skirt', 20, 19.99, 'FashionX', 'Apparel'),
('Camping Tent', 10, 149.99, 'OutdoorGear', 'Outdoor'),
('Blender', 25, 39.99, 'KitchenX', 'Kitchen'),
('Sports Bra', 30, 24.99, 'FitEquip', 'Fitness'),
('Dining Table', 15, 299.99, 'FurnitureCo', 'Furniture'),
('Basketball', 20, 24.99, 'SportsCo', 'Sports'),
('Desk Lamp', 25, 19.99, 'OfficeFurn', 'Home'),
('Hair Straightener', 20, 49.99, 'BeautyCo', 'Appliances'),
('Baseball Cap', 30, 14.99, 'FashionX', 'Accessories'),
('Hiking Boots', 15, 79.99, 'OutdoorGear', 'Footwear'),
('Pedometer', 25, 9.99, 'FitEquip', 'Fitness'),
('Cutting Board', 20, 14.99, 'KitchenX', 'Kitchen'),
('Tea Kettle', 15, 24.99, 'KitchenX', 'Kitchen'),
('Throw Pillow', 10, 19.99, 'HomeDecor', 'Home'),
('Curling Iron', 20, 29.99, 'BeautyCo', 'Appliances'),
('Soccer Jersey', 25, 39.99, 'SportsCo', 'Apparel'),
('Alarm Clock', 30, 19.99, 'TechCorp', 'Home'),
('Travel Backpack', 20, 49.99, 'PackCo', 'Accessories'),
('BBQ Grill', 10, 299.99, 'OutdoorGear', 'Outdoor'),
('Travel Mug', 25, 9.99, 'HydrateInc', 'Accessories'),
('Football', 20, 29.99, 'SportsCo', 'Sports'),
('Winter Gloves', 30, 19.99, 'OutdoorGear', 'Apparel'),
('Beanie', 25, 14.99, 'FashionX', 'Accessories'),
('Compact Mirror', 20, 9.99, 'BeautyCo', 'Accessories'),
('Snowboard', 10, 199.99, 'SportsCo', 'Outdoor');

UPDATE stock_tab
SET qty = qty - 1
WHERE sid = 1;

drop table stock_tab;

 create table customer(cid integer primary key auto_increment,cname varchar(30),cphone varchar(15),
 cemail varchar(30));
 select * from customer;
 
 insert into customer(cname,cphone,cemail) values('Anguraj',8220339605,'anguraj3125@gmail.com');
 
 select * from stock_tab;
 select * from stock_tab where sid =1;
 update stock_tab set pname ='Rin',qty=20,rate=12.00,manu='fssia',cata='soup' where sid=1;
 
 drop table customer;
commit