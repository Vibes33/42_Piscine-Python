from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class SpaceStation(BaseModel):
    """Pydantic model for space station data validation."""
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    print("Space Station Data Validation")
    print("=" * 40)

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-01-15T10:30:00",
        is_operational=True,
    )

    print("Valid station created:")
    print(f"  ID: {station.station_id}")
    print(f"  Name: {station.name}")
    print(f"  Crew: {station.crew_size} people")
    print(f"  Power: {station.power_level}%")
    print(f"  Oxygen: {station.oxygen_level}%")
    print(f"  Status: {'Operational' if station.is_operational else 'Offline'}")

    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Overflow Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance="2026-01-01T00:00:00",
        )
    except Exception as e:
        for err in e.errors():
            print(f"  {err['msg']}")


if __name__ == "__main__":
    main()
