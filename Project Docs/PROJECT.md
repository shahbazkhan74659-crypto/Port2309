# Project

## Overview

A personal portfolio website for the project owner — a single site intended to bring together their projects, writing, resume, and contact information in one place.

The site currently exists only as a single-page static visual prototype (`prototype/index.html`) using placeholder persona and content. No production backend or framework code has been written. See `ARCHITECTURE.md` for what actually exists, and `DECISIONS.md` for stack/architecture decisions made ahead of implementation.

## Problem

The project owner does not yet have a single place where visitors (recruiters, collaborators, readers) can find everything about them — projects, writing, resume, and a way to get in touch.

## Purpose

Build one site where anyone can find everything about the owner: Projects, Designs, Blogs, Resume, About Me, Contact, Skills, GitHub links, and a "Hire Me" feature.

## Goals

- A single, coherent site covering: Projects, Designs, Blog, Resume, About Me, Contact, Skills, GitHub links.
- A "Hire Me" feature.
- Server-rendered pages (Django templates) with targeted interactive pieces (React "islands") layered on top — not a full client-side SPA.

## Non-Goals

- Designs may be dropped from the site in the future — the feature is intended to be easy to remove without disturbing Projects, Blog, Resume, or Timeline. See `DECISIONS.md`.
- Not a full single-page application; React is intended for islands of interactivity only, not for driving overall page routing/rendering.

## Target Users

To be defined. (Implied audience, not yet explicitly confirmed by the owner: recruiters, collaborators, and readers of the owner's writing.)

## Core Features

Per prior planning discussion (see `DECISIONS.md`), the site is intended to cover:

- Projects
- Designs (removable/optional — see Non-Goals)
- Blog
- Resume
- About Me
- Contact
- Skills
- GitHub links
- A vertical Timeline of the owner's journey (college → now)
- "Hire Me" feature

The existing static prototype (`prototype/index.html`) currently demonstrates a subset of this: Home, Projects (list + detail), About, and Contact, using placeholder persona/content. It does not represent Designs, Resume, Skills, Timeline, or Hire Me. See `ARCHITECTURE.md`.

## Current Status

Planning phase, with one static visual prototype built. No production backend, framework, or database code exists. See `PHASES.md` and `TASKS.md`.

## Constraints

To be defined.

## Scope

A single-owner personal portfolio site. Not a multi-user or multi-tenant product.

## Success Criteria

To be defined.
