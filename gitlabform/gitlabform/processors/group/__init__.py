from typing import List, Optional, TextIO

from gitlabform.gitlab import GitLab
from gitlabform.gitlabform.processors.abstract_processor import AbstractProcessor
from gitlabform.gitlabform.processors.group.group_members_processor import (
    GroupMembersProcessor,
)
from gitlabform.gitlabform.processors.group.group_secret_variables_processor import (
    GroupSecretVariablesProcessor,
)
from gitlabform.gitlabform.processors.group.group_settings_processor import (
    GroupSettingsProcessor,
)


class GroupProcessors(object):
    def __init__(self, gitlab: GitLab):
        self.processors: List[AbstractProcessor] = [
            GroupSecretVariablesProcessor(gitlab),
            GroupSettingsProcessor(gitlab),
            GroupMembersProcessor(gitlab),
        ]

    def process_group(
        self,
        group: str,
        configuration: dict,
        dry_run: bool,
        output_file: Optional[TextIO],
    ):
        for processor in self.processors:
            processor.process(group, configuration, dry_run, output_file)
