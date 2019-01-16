DROP TABLE IF EXISTS `house`;

CREATE TABLE `house` (
  `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `username` varchar(20) NOT NULL DEFAULT '' COMMENT '用户名称',
  `phone` varchar(20) NOT NULL DEFAULT '' COMMENT '手机号码',
  `createDate` varchar(20) NOT NULL DEFAULT '' COMMENT '发布日期',
  `website` varchar(500) NOT NULL DEFAULT '' COMMENT '网站地址',
  `city` varchar(50) NOT NULL DEFAULT '' COMMENT '所属城市',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='租房信息';

