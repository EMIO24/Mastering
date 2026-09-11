"""Regenerate Week 1 instructional briefs without touching learner work or rubrics."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build():
    for number in range(1, 4):
        template = ROOT / 'tools' / 'assignment_briefs' / f'lesson-{number:02}.md.in'
        destination = ROOT / 'week-01' / 'assignments' / f'lesson-{number:02}' / 'README.md'
        destination.write_text(template.read_text(encoding='utf-8-sig'), encoding='utf-8')


if __name__ == '__main__':
    build()
