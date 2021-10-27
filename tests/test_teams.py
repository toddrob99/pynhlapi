import pynhlapi


class TestTeams():
    def test_team_by_id(self):
        nhl = pynhlapi.API()
        flyers = nhl.team_by_id(4)
        assert flyers["id"] == 4
        assert flyers["name"] == "Philadelphia Flyers"
        assert flyers["abbreviation"] == "PHI"
        assert flyers["teamName"] == "Flyers"
        assert flyers["shortName"] == "Philadelphia"
