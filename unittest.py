class TestPokerFunctions(unittest.TestCase):

    def test_check_straight(self):
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)
        self.assertEqual(check_straight('S6', 'S5', 'S7'), 7)
        self.assertEqual(check_straight('S3', 'SQ', 'SK'), 0)
        self.assertEqual(check_straight('S2', 'S3', 'SA'), 0)
        self.assertEqual(check_straight('S10', 'SJ', 'SQ'), 0)
        self.assertEqual(check_straight('S10', 'SJ', 'SA'), 14)

    def test_check_3ofa_kind(self):
        self.assertEqual(check_3ofa_kind('S9', 'S9', 'S9'), 9)
        self.assertEqual(check_3ofa_kind('S2', 'S4', 'S2'), 0)
        self.assertEqual(check_3ofa_kind('S10', 'SJ', 'SA'), 0)
        self.assertEqual(check_3ofa_kind('S3', 'S3', 'S3'), 3)

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('SA', 'SK', 'SQ'), 14)
        self.assertEqual(check_royal_flush('S10', 'SJ', 'SA'), 0)
        self.assertEqual(check_royal_flush('S9', 'SK', 'SQ'), 0)

    def test_play_cards(self):
        # Straights
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S8', 'S9', 'S10'), -1)
        self.assertEqual(play_cards('S9', 'S10', 'SJ', 'S6', 'S7', 'S8'), 1)
        self.assertEqual(play_cards('SA', 'S2', 'S3', 'SK', 'SQ', 'S10'), 0)

        # Three-of-a-kind
        self.assertEqual(play_cards('S9', 'S9', 'S9', 'S10', 'S10', 'S8'), -1)
        self.assertEqual(play_cards('SA', 'S9', 'S9', 'SK', 'SQ', 'SJ'), 1)
        self.assertEqual(play_cards('SA', 'S2', 'S2', 'SK', 'SQ', 'SJ'), 0)

        # Straight vs Three-of-a-kind
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S6', 'S6', 'S6'), -1)
        self.assertEqual(play_cards('S9', 'S10', 'SJ', 'SJ', 'SJ', 'S10'), 1)

        # Royal flush vs Straight
        self.assertEqual(play_cards('SA', 'SK', 'SQ', 'S9', 'S10', 'SJ'), -1)

        # Draw
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S6', 'S7', 'S5'), 0)
        self.assertEqual(play_cards('S9', 'S9', 'S9', 'SA', 'SA', 'SA'), 0)


if __name__ == '__main__':
    unittest.main()
