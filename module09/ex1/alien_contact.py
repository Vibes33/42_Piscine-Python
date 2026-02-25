from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, model_validator


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Pydantic model for alien contact log validation."""
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main():
    print("Alien Contact Log Validation")
    print("=" * 40)

    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2026-02-20T14:30:00",
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )

    print("Valid contact report:")
    print(f"  ID: {contact.contact_id}")
    print(f"  Type: {contact.contact_type.value}")
    print(f"  Location: {contact.location}")
    print(f"  Signal: {contact.signal_strength}/10")
    print(f"  Duration: {contact.duration_minutes} minutes")
    print(f"  Witnesses: {contact.witness_count}")
    print(f"  Message: '{contact.message_received}'")

    print("=" * 40)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2026-02-21T09:00:00",
            location="Bermuda Triangle",
            contact_type=ContactType.telepathic,
            signal_strength=3.0,
            duration_minutes=10,
            witness_count=1,
        )
    except Exception as e:
        for err in e.errors():
            print(f"  {err['msg']}")


if __name__ == "__main__":
    main()
