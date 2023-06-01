/*
 Navicat Premium Data Transfer

 Source Server         : tdex175
 Source Server Type    : MySQL
 Source Server Version : 50733
 Source Host           : 13.213.10.175:8005
 Source Schema         : exchange

 Target Server Type    : MySQL
 Target Server Version : 50733
 File Encoding         : 65001

 Date: 29/05/2023 11:28:08
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for mining_trade_fee_destroy
-- ----------------------------
DROP TABLE IF EXISTS `mining_trade_fee_destroy`;
CREATE TABLE `mining_trade_fee_destroy` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `add_time` int(11) DEFAULT NULL,
  `contract_address` varchar(100) DEFAULT NULL,
  `destroy_count` decimal(60,0) DEFAULT NULL,
  `block_height` int(10) unsigned DEFAULT NULL,
  `from_address` varchar(100) DEFAULT NULL,
  `to_address` varchar(100) DEFAULT NULL,
  `chain_id` int(11) DEFAULT NULL,
  `tx_hash` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of mining_trade_fee_destroy
-- ----------------------------
BEGIN;
INSERT INTO `mining_trade_fee_destroy` (`id`, `add_time`, `contract_address`, `destroy_count`, `block_height`, `from_address`, `to_address`, `chain_id`, `tx_hash`) VALUES (117, 1681099784, '0x17a011150e9Feb7bEc4CfAda055c8Df436EB730B', 81458814083600000000000, 41354167, '0xaE7de6Bc7Ea6Ee597e7274F688615C60eEF7Ecb8', '0x0000000000000000000000000000000000000000', 137, '0x50824071aea5bac6318d7ad499f12095a159e657d551c0f578d87f59b843ce74');
INSERT INTO `mining_trade_fee_destroy` (`id`, `add_time`, `contract_address`, `destroy_count`, `block_height`, `from_address`, `to_address`, `chain_id`, `tx_hash`) VALUES (118, 1681704367, '0x17a011150e9Feb7bEc4CfAda055c8Df436EB730B', 58037426931200000000000, 41621601, '0xaE7de6Bc7Ea6Ee597e7274F688615C60eEF7Ecb8', '0x0000000000000000000000000000000000000000', 137, '0x6dc0362db43eb07e998aac9205bd235e9decc6fa49f67b046d2a147c39fe2018');
INSERT INTO `mining_trade_fee_destroy` (`id`, `add_time`, `contract_address`, `destroy_count`, `block_height`, `from_address`, `to_address`, `chain_id`, `tx_hash`) VALUES (119, 1682324919, '0x17a011150e9Feb7bEc4CfAda055c8Df436EB730B', 62992621681200000000000, 41895522, '0xaE7de6Bc7Ea6Ee597e7274F688615C60eEF7Ecb8', '0x0000000000000000000000000000000000000000', 137, '0xd279fd490fe80dee527e5775a2eb6674f8cd627295b047b81fd491712bd7f5c2');
INSERT INTO `mining_trade_fee_destroy` (`id`, `add_time`, `contract_address`, `destroy_count`, `block_height`, `from_address`, `to_address`, `chain_id`, `tx_hash`) VALUES (120, 1682911640, '0x17a011150e9Feb7bEc4CfAda055c8Df436EB730B', 67507449530000000000000, 42160948, '0xaE7de6Bc7Ea6Ee597e7274F688615C60eEF7Ecb8', '0x0000000000000000000000000000000000000000', 137, '0x74bd0abab66664b7ed81c35235c78afb58b47e9647b3e94d6b91dcd5bcc1f088');
INSERT INTO `mining_trade_fee_destroy` (`id`, `add_time`, `contract_address`, `destroy_count`, `block_height`, `from_address`, `to_address`, `chain_id`, `tx_hash`) VALUES (121, 1683531711, '0x17a011150e9Feb7bEc4CfAda055c8Df436EB730B', 53387817386000000000000, 42445256, '0xaE7de6Bc7Ea6Ee597e7274F688615C60eEF7Ecb8', '0x0000000000000000000000000000000000000000', 137, '0x0063a950764e8a993215a078db133d3b9189ce52cfa2e8a52bef2a8da577e6d6');
INSERT INTO `mining_trade_fee_destroy` (`id`, `add_time`, `contract_address`, `destroy_count`, `block_height`, `from_address`, `to_address`, `chain_id`, `tx_hash`) VALUES (122, 1684132122, '0x17a011150e9Feb7bEc4CfAda055c8Df436EB730B', 56620039187600000000000, 42724392, '0xaE7de6Bc7Ea6Ee597e7274F688615C60eEF7Ecb8', '0x0000000000000000000000000000000000000000', 137, '0x36180c55cc56b651c0700b6ee0a867458a6478414a3f58d51cb8249c4c33f5c9');
INSERT INTO `mining_trade_fee_destroy` (`id`, `add_time`, `contract_address`, `destroy_count`, `block_height`, `from_address`, `to_address`, `chain_id`, `tx_hash`) VALUES (123, 1684735879, '0x17a011150e9Feb7bEc4CfAda055c8Df436EB730B', 51804753159400000000000, 43003607, '0xaE7de6Bc7Ea6Ee597e7274F688615C60eEF7Ecb8', '0x0000000000000000000000000000000000000000', 137, '0xafd562b876c9597bcfe2ddfb05fe42539a3391ed91a8df6f272a67410348f9c8');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
