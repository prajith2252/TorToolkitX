# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]

import logging
from abc import ABC, abstractmethod
from typing import BinaryIO, Union

TorLog = logging.getLogger(__name__)


class AbstractDatabase(ABC):
    @abstractmethod
    def set_variable(
        self,
        var_name: str,
        var_value: Union[list, str, int],
        update_blob: bool = False,
        blob_value: BinaryIO = None,
    ) -> None:

        ...

    @abstractmethod
    def get_variable(self, var_name: str) -> Union[str, int, list, BinaryIO]:

        ...
