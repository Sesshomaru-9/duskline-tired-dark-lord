# Duskline Tired Dark Lord

Entry for [The Tired Dark Lord: A 100-Word Villain Monologue](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb) (make.fun, $2, 10 places).

## The monologue (97 words, 505 characters)

> Right. The hero. I saw the sword. Sit—not the throne, the stool. Three hundred years I waited in the dark. I had a speech. I had lightning. I had—where did I put the lightning? Never mind. The point is, boy, I won. Nine kingdoms kneel, the dragons file their taxes on time, the prophecy is... filed. Under P. Now you want a duel at dawn. Dawn. I have a grain levy at dawn, and the trolls want the bridge tolls cut. So. Kneel, swear, take the east wing, and we shall fight... Tuesday. Bring your own lunch.

The Dark Lord has already won — three hundred years in the dark, nine kingdoms kneeling, dragons filing taxes on time — and now victory turns out to be administration: a grain levy, troll bridge tolls, a prophecy filed under P. The exhaustion never gets announced; it lives in the pauses, the lost lightning, the repeated "Dawn.", and the deflections ("Never mind", "So."). The sting lands in the last line: the fated duel is rescheduled to Tuesday, and the hero is told to bring his own lunch.

## How the program works

`main.py` (Python 3.13, standard library only, deterministic, no network) writes the monologue above to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to a fresh temporary directory when the variable is unset). It validates the text against the gate first — UTF-8, 1–600 characters, not only whitespace — writes the file, then reads it back and verifies it matches byte for byte. It never raises: any failure exits 0 without writing anything. A hard guard refuses to write if the resolved output directory is the repository directory or inside it.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.
