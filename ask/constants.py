import datetime


YEAR = datetime.datetime.today().year

NALOG_CHOICES = (
    (0, 'Данные отсутствуют'),
    (1,  'ЕНВД'),
    (2, 'УСН'),
    (3, 'Не применяется'),
)

SMSP_CHOICES = (
    (1, 'Микропредприятие'),
    (2, 'Малое предприятие'),
    (3, 'Среднее предприятие'),
    (4, 'Не входит'),
)

OKOPF_CHOICES = (
    (12247, 12247),
    (12267, 12267),
    (12300, 12300),
    (70400, 70400),
    (71400, 71400),
    (75204, 75204),
)

OKFS_CHOICES = (
    (12, 12),
    (13, 13),
    (16, 16),
    (23, 23),
    (24, 24),
    (27, 27),
    (34, 34),
    (42, 42),
    (49, 49),
    (53, 53),
)

BASE_OKVED_CHOICES = (
    (267, '01.49.1'),
    (61, '08.11'),
    (104, '08.99.23'),
    (222, '10.51'),
    (198, '10.71'),
    (170, '10.72'),
    (74, '11.02'),
    (86, '13.92'),
    (133, '13.95'),
    (39, '13.96'),
    (129, '13.99.9'),
    (256, '15.12'),
    (67, '16.10'),
    (139, '16.21.1'),
    (84, '16.23'),
    (279, '16.23.1'),
    (95, '16.29.1'),
    (151, '17.2'),
    (54, '17.24'),
    (227, '18.14'),
    (268, '20.11'),
    (111, '20.16'),
    (12, '20.30'),
    (144, '20.30.1'),
    (152, '20.30.2'),
    (138, '20.52'),
    (261, '20.59.5'),
    (109, '22.1'),
    (114, '22.2'),
    (3, '22.21'),
    (87, '22.23'),
    (145, '22.29'),
    (121, '22.29.2'),
    (123, '23.12'),
    (110, '23.19.2'),
    (162, '23.20'),
    (88, '23.31'),
    (9, '23.32'),
    (117, '23.51'),
    (146, '23.52.2'),
    (8, '23.6'),
    (18, '23.61'),
    (28, '23.62'),
    (45, '23.63'),
    (65, '23.64'),
    (15, '23.65'),
    (13, '23.69'),
    (52, '23.70'),
    (140, '23.91'),
    (50, '23.99'),
    (16, '23.99.2'),
    (100, '23.99.6'),
    (4, '24.33'),
    (259, '24.34'),
    (113, '25.1'),
    (26, '25.11'),
    (97, '25.12'),
    (157, '25.21'),
    (25, '25.30.1'),
    (23, '25.50'),
    (21, '25.62'),
    (160, '25.72'),
    (141, '25.93'),
    (101, '25.99'),
    (147, '25.99.21'),
    (56, '26.40'),
    (153, '26.51.2'),
    (180, '27.3'),
    (137, '27.32'),
    (159, '27.4'),
    (33, '27.40'),
    (286, '27.51'),
    (71, '27.52'),
    (216, '27.9'),
    (43, '27.90'),
    (260, '28.1'),
    (20, '28.12'),
    (94, '28.21'),
    (24, '28.22'),
    (44, '28.22.6'),
    (135, '28.25.2'),
    (119, '28.29'),
    (78, '28.29.1'),
    (228, '28.30.85'),
    (77, '28.41'),
    (98, '28.92'),
    (236, '28.93'),
    (53, '28.99'),
    (122, '28.99.9'),
    (132, '29.10.05'),
    (38, '31.09'),
    (42, '32.91'),
    (62, '32.99'),
    (51, '32.99.8'),
    (79, '32.99.9'),
    (149, '33.12'),
    (271, '33.14'),
    (75, '35.11.4'),
    (126, '35.30'),
    (226, '36.00'),
    (37, '36.00.1'),
    (285, '38.32.3'),
    (134, '41.2'),
    (11, '41.20'),
    (107, '42.21'),
    (158, '43.12'),
    (167, '43.21'),
    (120, '43.22'),
    (5, '43.31'),
    (184, '43.32'),
    (244, '43.32.1'),
    (48, '43.33'),
    (266, '43.39'),
    (6, '43.99'),
    (274, '43.99.5'),
    (161, '45.1'),
    (115, '45.19'),
    (124, '45.2'),
    (251, '45.20'),
    (238, '45.20.1'),
    (269, '45.20.3'),
    (102, '45.3'),
    (252, '45.31.1'),
    (220, '45.32'),
    (128, '46.1'),
    (64, '46.13.2'),
    (99, '46.15.3'),
    (130, '46.15.9'),
    (154, '46.18'),
    (82, '46.19'),
    (233, '46.3'),
    (223, '46.38'),
    (273, '46.38.1'),
    (70, '46.4'),
    (255, '46.42'),
    (55, '46.43'),
    (35, '46.43.1'),
    (150, '46.44.1'),
    (172, '46.44.2'),
    (243, '46.46.1'),
    (281, '46.46.2'),
    (116, '46.47'),
    (164, '46.47.3'),
    (46, '46.49'),
    (214, '46.49.33'),
    (155, '46.49.4'),
    (59, '46.49.49'),
    (235, '46.51'),
    (30, '46.51.2'),
    (2, '46.6'),
    (76, '46.61'),
    (68, '46.62'),
    (92, '46.63'),
    (47, '46.69'),
    (163, '46.69.2'),
    (125, '46.69.3'),
    (58, '46.69.5'),
    (90, '46.69.9'),
    (156, '46.7'),
    (272, '46.71'),
    (258, '46.72'),
    (49, '46.72.2'),
    (183, '46.72.22'),
    (1, '46.73'),
    (96, '46.73.1'),
    (19, '46.73.3'),
    (7, '46.73.4'),
    (10, '46.73.6'),
    (131, '46.73.7'),
    (105, '46.73.8'),
    (14, '46.74'),
    (89, '46.74.2'),
    (36, '46.74.3'),
    (22, '46.75'),
    (148, '46.75.2'),
    (106, '46.76'),
    (31, '46.90'),
    (194, '47.1'),
    (171, '47.11'),
    (248, '47.11.1'),
    (224, '47.11.2'),
    (278, '47.11.3'),
    (193, '47.19'),
    (254, '47.19.1'),
    (231, '47.19.2'),
    (187, '47.2'),
    (240, '47.22.2'),
    (174, '47.24'),
    (186, '47.25'),
    (176, '47.25.1'),
    (215, '47.25.11'),
    (188, '47.29'),
    (175, '47.30'),
    (246, '47.41'),
    (242, '47.43'),
    (247, '47.5'),
    (83, '47.52'),
    (276, '47.52.1'),
    (282, '47.52.2'),
    (17, '47.52.7'),
    (263, '47.52.71'),
    (27, '47.52.72'),
    (80, '47.52.73'),
    (136, '47.53'),
    (81, '47.53.2'),
    (179, '47.53.3'),
    (72, '47.54'),
    (206, '47.59'),
    (284, '47.59.1'),
    (250, '47.59.2'),
    (239, '47.59.3'),
    (234, '47.61'),
    (262, '47.62'),
    (210, '47.62.2'),
    (200, '47.7'),
    (264, '47.71'),
    (229, '47.71.1'),
    (185, '47.73'),
    (212, '47.74'),
    (225, '47.75'),
    (232, '47.76.1'),
    (169, '47.77.2'),
    (245, '47.78'),
    (209, '47.78.9'),
    (208, '47.82'),
    (69, '47.91.2'),
    (219, '49.3'),
    (257, '49.32'),
    (221, '49.39'),
    (190, '49.39.11'),
    (108, '49.4'),
    (173, '49.41'),
    (283, '49.41.1'),
    (182, '49.41.2'),
    (241, '49.42'),
    (177, '52.10'),
    (213, '52.21.24'),
    (166, '52.29'),
    (197, '55.10'),
    (201, '56.1'),
    (165, '56.10'),
    (203, '56.10.1'),
    (207, '56.29'),
    (218, '56.29.2'),
    (192, '56.30'),
    (211, '58.11'),
    (280, '58.19'),
    (189, '59.14'),
    (142, '61.10'),
    (29, '62.02'),
    (40, '62.03'),
    (275, '62.09'),
    (143, '63.11'),
    (249, '63.11.1'),
    (57, '64.20'),
    (63, '64.92.2'),
    (93, '64.99'),
    (32, '66.22'),
    (230, '68.2'),
    (196, '68.20'),
    (204, '68.20.1'),
    (195, '68.20.2'),
    (199, '68.32'),
    (112, '70.10.1'),
    (66, '70.22'),
    (41, '71.1'),
    (118, '71.11.1'),
    (127, '71.12.45'),
    (237, '71.20.5'),
    (103, '72.1'),
    (91, '72.19'),
    (34, '73.11'),
    (181, '73.20.1'),
    (178, '74.90.22'),
    (85, '77.39'),
    (60, '79.11'),
    (253, '81.29.9'),
    (73, '84.11.21'),
    (168, '86.21'),
    (202, '95.11'),
    (270, '95.21'),
    (277, '96.01'),
    (217, '96.02'),
    (191, '96.03'),
    (205, '96.04'),
)
