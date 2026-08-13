# Privacy Policy for Ohara

**Last updated: 13 August 2026**

Ohara is a log for One Piece Card Game tournaments. You record the
events you played, who you played, what you brought and how it went, and the
app works out your record and your matchups.

The short version: your log lives on your phone. You do not need an account to
use the app. Your log only goes to a server if you make an account and press
Sync, and even then it goes to your account and nowhere else. Nobody else can
see it. There are no ads, no analytics and no tracking of any kind.

## What is stored on your phone

Everything you enter, in a database on the device:

- events — name, store, date, category, the deck you brought, your placement;
- rounds — result, dice roll, play order, the opposing leader, your notes;
- opponents — a name, an optional Bandai membership number, optional notes, and
  an optional photo if you add one;
- final standings for an event — the names, member numbers and finishes of
  everyone in the room, if you import or type them;
- your settings, like theme, and whether you chose to use the app without an
  account.

If you delete the app, all of it goes with it. Nothing is recovered unless you
exported a backup or synced.

## Do you need an account?

No. The first screen offers **Continue as guest**, and a guest gets the whole
app — logging, stats, screenshot import, export and backup. The only thing an
account adds is sync, so your log survives losing your phone and appears on a
second device. You are asked once; after that the app opens straight into your
log.

If you do make an account, we use **Sign in with Apple**. Apple tells us an
account identifier and an email address. If you choose "Hide My Email", Apple
gives us a relay address instead of your real one and we never see your real
one. We use the email only to identify your account and to show you which
account you are signed in to. We do not send marketing email.

## What leaves your phone

Only if you sign in, and only when you press **Sync now** in Settings. The app
never syncs on its own — not on launch, not when you save a round, not in the
background. If you never sign in, nothing you enter ever leaves the device.

When you do sync, these go to your account on our server: your events, your
rounds, your stores, and your opponents including their names, membership
numbers, notes and photos.

**Final standings never leave your phone.** The rest of the room — everyone
else's names and finishes from an imported standings screen — is deliberately
kept on the device and is not part of sync or of the backup file.

Your data is stored in a database where every row is locked to your account.
Other people using the app cannot read your rows, and you cannot read theirs.
There is nothing social in the app: no profiles, no friends, no feed, no
sharing between users.

## Screenshots you import

You can import a Bandai match-history or standings screenshot instead of typing
it in. The text is read out of the image **on your phone**, by software running
on the device. The image is never uploaded and the app never saves a copy of
it. Only the text the app read — names, results, points — is kept, and only in
your log on your phone.

One honest detail: the system photo picker may leave its own temporary copy of
the image in the app's cache, which is how iOS hands a photo to an app. The app
never reads that copy, never keeps it and never uploads it, and iOS clears the
cache in its own time.

## Photos you add

You can attach a photo to an opponent. It is stored in your log on the device,
and it is included in a sync if you sync. It is not shared with anyone else and
not uploaded anywhere except your own account.

## Backups you make yourself

Settings can export your whole log as a file. That file is handed to your
phone's share sheet and goes wherever you send it — it is your file, and where
it ends up is your choice. It contains your events, rounds, stores and
opponents including photos. It does not contain standings.

The app can also make a picture of an event recap to share. If that event has
standings, the picture shows the names in them. You choose whether to share it
and with whom.

## Who else is involved

Three, and no others:

- **Apple**, if you sign in — Sign in with Apple handles the sign-in and tells
  us an account identifier and an email address.
- **Supabase**, if you sync — the hosting provider that runs the database your
  account lives in. The database is in Montreal, Canada. Supabase stores the
  data for us and does not use it for anything of its own.
- **Google's ML Kit**, for reading screenshots — a text recogniser that runs
  entirely on your phone. It is part of the app, not a service; no image and no
  text is sent anywhere.

No advertising network, no analytics service and no crash reporter receives
anything, because the app contains none.

## What we do not do

- No advertising, and no ad networks.
- No analytics, no usage tracking, no crash reporting. The app contains no
  such software at all.
- No tracking across apps or websites, so the app never asks for permission to
  track.
- No selling or sharing of your data with anyone.
- No profiling, no automated decisions about you.

## Deleting your data, and how long we keep it

- **Delete one thing:** delete an event, a round or an opponent in the app. If
  you sync, the deletion travels on your next sync.
- **Delete your account and everything synced:** Settings → Delete account. It
  removes your account and every event, round, store and opponent copied to the
  server. It is permanent and cannot be undone.
- **Your log stays on your phone when you delete your account.** That is
  deliberate — deleting the copy on the server should not take your history
  with it. To remove the log itself, delete the app.
- **Sign out** leaves everything as it is, on both the phone and the server.

We keep synced data for as long as your account exists. We do not delete it on
a schedule and we do not archive it anywhere else. When you delete your
account, it goes from the live database straight away. Our hosting provider may
still hold it briefly in its own routine database backups, which roll off on
their schedule; those are the provider's and are used only to restore the
database after a failure.

## Children

The app is not directed at children and asks for nothing about age. It stores
only what you type into it.

## Changes to this policy

If this changes, the date at the top changes and the new version is published
at https://buckelew.github.io/ohara-privacy/. Significant changes will be noted in the app's
release notes.

## Your rights

Depending on where you live you may have the right to see, correct, export or
delete the data held about you. The app gives you all four directly: your log
is on your phone, you can edit or delete anything in it, Export makes you a
copy, and Delete account removes the server copy. If you want anything else,
write to buckelew.02@gmail.com.

## Contact

Ohara is made by one person, not a company.

Caden Buckelew
buckelew.02@gmail.com

I develop and run Ohara from Oregon, USA, and this policy is governed by
the laws that apply there.
