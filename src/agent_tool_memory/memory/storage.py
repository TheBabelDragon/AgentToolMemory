"""Storage backend interface for structured agent memory."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from agent_tool_memory.memory.models import MemoryRecord, RecordType


class MemoryBackend(ABC):
    """Replaceable persistence backend. Memory is never authorization."""

    @abstractmethod
    def append(self, record: MemoryRecord) -> None:
        """Append a new record. Must not overwrite existing record_id."""

    @abstractmethod
    def get(self, record_id: str) -> Optional[MemoryRecord]:
        ...

    @abstractmethod
    def filter(
        self,
        *,
        subject: Optional[str] = None,
        record_type: Optional[RecordType] = None,
        related_to: Optional[str] = None,
        tags: Optional[List[str]] = None,
        active_only: bool = True,
        since: Optional[str] = None,
        until: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> List[MemoryRecord]:
        """Return matching records ordered by timestamp ascending."""

    @abstractmethod
    def supersede(self, record_id: str, successor_id: str) -> bool:
        """
        Mark record_id as superseded by successor_id.
        Historical content is preserved; only the pointer changes.
        Returns True if the record existed and was updated.
        """

    @abstractmethod
    def count(self, subject: Optional[str] = None) -> int:
        ...

    @abstractmethod
    def close(self) -> None:
        ...
