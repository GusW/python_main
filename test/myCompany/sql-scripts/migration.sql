CREATE TABLE t_shops_offline_availability (
    a_shop_id       INT(11)         NOT NULL REFERENCES t_shops (a_id),
    a_month         DATE            NOT NULL,
    a_budget_amount DECIMAL(10,2)   NOT NULL,
    PRIMARY KEY (a_shop_id, a_month, a_budget_amount)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE t_budget_notification_types (
    a_id        INT(11)         NOT NULL AUTO_INCREMENT,
    a_name      VARCHAR(255)    NOT NULL,
    a_target    DECIMAL(10,2)   NOT NULL,
    PRIMARY KEY (a_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE t_budget_notifications (
    a_shop_id   INT(11)         NOT NULL REFERENCES t_shops (a_id),
    a_month     DATE            NOT NULL,
    a_amount    DECIMAL(10,2)   NOT NULL,
    a_type_id   INT(11)         NOT NULL REFERENCES t_budget_notification_types (a_id),
    a_message   TEXT(512)       NOT NULL,
    a_sent_in   DATE            NOT NULL,
    PRIMARY KEY (a_shop_id, a_month, a_amount, a_type_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO t_budget_notification_types
    (a_id,  a_name,                     a_target)
VALUES
    (1,     'Half budget consumption',  50),
    (2,     'Full budget consumption',  100);


INSERT INTO t_budgets
    (a_shop_id, a_month, a_budget_amount, a_amount_spent)
VALUES
    (1, '2020-08-01', 930.00, 925.67),
    (2, '2020-08-01', 990.00, 886.63),
    (3, '2020-08-01', 650.00, 485.91),
    (4, '2020-08-01', 740.00, 346.92),
    (5, '2020-08-01', 630.00, 207.64),
    (6, '2020-08-01', 640.00, 246.32),
    (7, '2020-08-01', 980.00, 940.16),
    (8, '2020-08-01', 790.00, 265.64),
    (1, '2020-09-01', 960.00, 103.67),
    (2, '2020-09-01', 670.00, 915.64),
    (3, '2020-09-01', 890.00, 980.81),
    (4, '2020-09-01', 590.00, 754.93),
    (5, '2020-09-01', 870.00, 905.12),
    (6, '2020-09-01', 700.00, 912.30),
    (7, '2020-09-01', 990.00, 905.15),
    (8, '2020-09-01', 720.00, 604.25),
    (1, '2020-10-01', 960.00, 953.67),
    (2, '2020-10-01', 670.00, 515.64),
    (3, '2020-10-01', 890.00, 890.01),
    (4, '2020-10-01', 590.00, 354.93),
    (5, '2020-10-01', 870.00, 805.12),
    (6, '2020-10-01', 700.00, 912.30),
    (7, '2020-10-01', 990.00, 905.15),
    (8, '2020-10-01', 720.00, 804.25);

ALTER TABLE t_shops
DROP COLUMN a_online;
