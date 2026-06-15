"""Cortex AuthorForge service surface.

A thin, bounded HTTP front door over ``cortex_runtime`` that exposes exactly the
file-intelligence seam AuthorForge consumes. It adds no semantics, no workflow
control, and no durable truth — it adapts ``cortex_runtime`` results into the
AuthorForge contract and holds a bounded, TTL'd retrieval artifact cache only.

See ADR 0004 (Cortex boundary): syntax-before-semantics. Entity identification
and any semantic interpretation are explicitly refused here and left to
NeuronForge via AuthorForge's own orchestration.
"""
