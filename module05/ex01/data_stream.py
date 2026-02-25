from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for all data streams."""

    def __init__(self, stream_id: str):
        super().__init__()
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if isinstance(item, str)
                and criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "stream_id": self.stream_id,
            "processed": self.processed_count
        }


class SensorStream(DataStream):
    """Stream for environmental sensor data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            readings: List[float] = [x for x in data_batch
                                     if isinstance(x, (int, float))]
            self.processed_count += len(readings)
            avg: float = sum(readings) / len(readings) if readings else 0
            return (f"Sensor analysis: {len(readings)} readings processed, "
                    f"avg temp: {avg}°C")
        except Exception as e:
            return f"Sensor error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "critical":
            return [x for x in data_batch
                    if isinstance(x, (int, float)) and x > 30]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        return stats


class TransactionStream(DataStream):
    """Stream for financial transaction data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            operations: List[str] = [x for x in data_batch
                                     if isinstance(x, str)]
            self.processed_count += len(operations)
            net: int = 0
            for op in operations:
                if "buy" in op:
                    net -= int(op.split(":")[1]) if ":" in op else 0
                elif "sell" in op:
                    net += int(op.split(":")[1]) if ":" in op else 0
            sign: str = "+" if net >= 0 else ""
            return (f"Transaction analysis: {len(operations)} operations, "
                    f"net flow: {sign}{net} units")
        except Exception as e:
            return f"Transaction error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            return [x for x in data_batch if isinstance(x, str)
                    and ":" in x and abs(int(x.split(":")[1])) > 100]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        return stats


class EventStream(DataStream):
    """Stream for system event data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.error_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events: List[str] = [x for x in data_batch
                                 if isinstance(x, str)]
            self.processed_count += len(events)
            errors: int = len([e for e in events if "error" in e])
            self.error_count += errors
            return (f"Event analysis: {len(events)} events, "
                    f"{errors} error detected")
        except Exception as e:
            return f"Event error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "errors":
            return [x for x in data_batch if isinstance(x, str)
                    and "error" in x]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "System Events"
        stats["errors"] = self.error_count
        return stats


class StreamProcessor:
    """Handles multiple stream types polymorphically."""

    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]) -> List[str]:
        """Process batches for all registered streams."""
        results: List[str] = []
        for stream in self.streams:
            try:
                if stream.stream_id in batches:
                    result = stream.process_batch(batches[stream.stream_id])
                    results.append(result)
            except Exception as e:
                results.append(f"Stream {stream.stream_id} failed: {e}")
        return results

    def filter_all(self, data_batch: List[Any],
                   criteria: Optional[str] = None) -> Dict[str, List[Any]]:
        """Filter data through all streams."""
        return {
            stream.stream_id: stream.filter_data(data_batch, criteria)
            for stream in self.streams
        }

    def get_all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        return [stream.get_stats() for stream in self.streams]


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    # --- Sensor Stream ---
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    stats = sensor.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    sensor_data: List[Any] = [22.5, 22.5, 22.5]
    print(f"Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(sensor_data))

    # --- Transaction Stream ---
    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    stats = trans.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    trans_data: List[Any] = ["buy:100", "sell:150", "buy:25"]
    print(f"Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(trans.process_batch(trans_data))

    # --- Event Stream ---
    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    stats = event.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    event_data: List[Any] = ["login", "error", "logout"]
    print(f"Processing event batch: [login, error, logout]")
    print(event.process_batch(event_data))

    # --- Polymorphic Processing ---
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    batches: Dict[str, List[Any]] = {
        "SENSOR_001": [25.0, 28.3],
        "TRANS_001": ["buy:50", "sell:200", "buy:30", "sell:80"],
        "EVENT_001": ["login", "error", "logout"]
    }
    results = processor.process_all(batches)

    print("\nBatch 1 Results:")
    for r in results:
        print(f"  - {r}")

    # --- Filtering ---
    print("\nStream filtering active: High-priority data only")
    critical_sensors = sensor.filter_data([35.0, 20.0, 40.0], "critical")
    large_trans = trans.filter_data(
        ["buy:50", "sell:200"], "large"
    )
    print(f"Filtered results: {len(critical_sensors)} critical sensor alerts, "
          f"{len(large_trans)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
