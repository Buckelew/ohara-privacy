"""Build an Anki deck (.apkg) plus a plain TSV from the per-category JSON card files.

Usage: python3 build_deck.py <cards_dir> <out_dir>
"""
import csv
import hashlib
import html
import json
import sys
from pathlib import Path

import genanki
from anki.collection import Collection, ExportAnkiPackageOptions, ImportAnkiPackageRequest, ImportAnkiPackageOptions

CATEGORIES = {
    "1_music_festivals": "01 Music Festivals",
    "2_famous_pumpkins": "02 Famous Pumpkins (Picture Round)",
    "3_what_are_you_afraid_of": "03 What Are You Afraid Of",
    "4_l_artists": "04 L Artists Music Round",
    "6_stephen_king": "05 The King of Horror",
    "7_religion": "06 Losing My Religion",
}

MODEL = genanki.Model(
    1607392319,
    "Trivia Q/A",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Category"}],
    templates=[{
        "name": "Card 1",
        "qfmt": '<div class="cat">{{Category}}</div><div class="q">{{Front}}</div>',
        "afmt": '{{FrontSide}}<hr id="answer"><div class="a">{{Back}}</div>',
    }],
    css=""".card{font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:22px;text-align:center;}
.cat{font-size:13px;opacity:.6;text-transform:uppercase;letter-spacing:.05em;margin-bottom:12px}
.a{font-weight:600} img{max-width:90%;max-height:320px}""",
)


class Note(genanki.Note):
    @property
    def guid(self):
        return genanki.guid_for(self.fields[2], self.fields[0])


def stable_id(name):
    return int(hashlib.sha1(name.encode()).hexdigest()[:8], 16) + (1 << 30)


def embed_cram_preset(apkg):
    """Re-export the package through Anki itself with a one-week cram preset on every deck."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        col = Collection(f"{tmp}/c.anki2")
        col.import_anki_package(ImportAnkiPackageRequest(
            package_path=str(apkg), options=ImportAnkiPackageOptions()))
        conf = col.decks.add_config_returning_id("Trivia Cram (1 week)")
        conf = col.decks.get_config(conf)
        conf["new"].update(perDay=42, delays=[1.0, 10.0], ints=[1, 2, 0])
        conf["rev"].update(perDay=9999, maxIvl=2)
        conf["lapse"].update(delays=[10.0], minInt=1)
        conf["newGatherPriority"] = 4  # random cards, so rounds are mixed
        col.decks.update_config(conf)
        for d in col.decks.all_names_and_ids():
            if d.name.startswith("Trivia Night"):
                deck = col.decks.get(d.id)
                deck["conf"] = conf["id"]
                col.decks.save(deck)
        col.export_anki_package(
            out_path=str(apkg),
            options=ExportAnkiPackageOptions(with_deck_configs=True, with_scheduling=False, with_media=False),
            limit=None,
        )
        col.close()


def main(cards_dir, out_dir):
    cards_dir, out_dir = Path(cards_dir), Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    decks, rows = [], []
    for stem, title in CATEGORIES.items():
        path = cards_dir / f"{stem}.json"
        if not path.exists():
            print(f"missing {path}")
            continue
        tiers = {
            "core": genanki.Deck(stable_id(stem), f"Trivia Night::1 Core::{title}"),
            "bonus": genanki.Deck(stable_id(stem + "_bonus"), f"Trivia Night::2 Bonus::{title}"),
        }
        seen = set()
        for c in json.load(open(path)):
            priority = c.get("priority", "core")
            front, back = c["front"].strip(), c["back"].strip()
            if front.lower() in seen:
                continue
            seen.add(front.lower())
            tags = [t.replace(" ", "_") for t in c.get("tags", [])] + [stem, priority]
            tiers[priority].add_note(Note(model=MODEL, fields=[html.escape(front), html.escape(back), title], tags=tags))
            rows.append([front, back, title, " ".join(tags)])
        print(f"{title}: {len(tiers['core'].notes)} core, {len(tiers['bonus'].notes)} bonus")
        decks.extend(tiers.values())
    apkg = out_dir / "trivia_night.apkg"
    genanki.Package(decks).write_to_file(apkg)
    embed_cram_preset(apkg)
    with open(out_dir / "trivia_night.tsv", "w", newline="") as f:
        csv.writer(f, delimiter="\t").writerows(rows)
    print(f"total: {len(rows)} cards")


if __name__ == "__main__":
    main(*sys.argv[1:3])
