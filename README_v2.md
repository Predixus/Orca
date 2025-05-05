# Orca

Orca is a free and open-source (FOSS) analytics orchestration framework that makes it easy for development and product teams to extract insights from timeseries data. It provides a structured and scalable way to schedule, process, and analyze data using a flexible DAG-based architecture.

## ✨ Features

- **Pluggable processors:** Register processors dynamically and scale horizontally.
- **Window-based execution:** Define regions of interest (windows) to trigger algorithms.
- **DAG execution engine:** Automatically handles dependencies and triggers algorithms.
- **PostgreSQL support:** Built-in datalayer for Postgres, with extensibility for others.
- **gRPC API:** Fast and language-agnostic communication.

## 🚀 Getting Started

### 1. Install Orca

Clone the repo:

```bash
git clone https://github.com/predixus/orca.git
cd orca
```

Build the binary:

```bash
make build
```

### 2. Setup Database

Start a local PostgreSQL instance with:

```bash
make build_store
```

Other DB commands:

```bash
make start_store    # start DB
make stop_store     # stop DB
make remove_store   # delete DB and data
make redo_store     # reset DB
```

### 3. Run Orca Core

```bash
./orca --platform postgresql --db "postgresql://user:pass@localhost:5432/orca" --port 50051
```

### 4. Register a Processor

Use gRPC or a client library to register processors and algorithms. Processors should implement the `OrcaProcessor` gRPC interface.

---

## 📦 Architecture

1. Processors register with the Orca Core service.
2. Windows are emitted into the system.
3. Orca builds an execution DAG from dependencies.
4. Tasks are streamed to processors.
5. Results return to the core.
6. Dependent algorithms are triggered automatically.

---

## 🔌 Extending Orca

To implement a custom datalayer, your driver must implement:

- `CreateProcessor`
- `EmitWindow`

See `internal/datalayers/types.go` for the interface.

---

## 💻 Development

### Install proto tools

```bash
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
python -m pip install grpcio grpcio-tools
```

### Generate docs (optional)

```bash
docker pull pseudomuto/protoc-gen-doc
```

---

## 📜 Rules

1. Algorithm DAGs can only be triggered by a single WindowType.
2. Algorithms can’t depend on algorithms from a different WindowType.

---

## 💬 Community

- Issues: [GitHub Issues](https://github.com/predixus/orca/issues)
- Discussions: Coming soon!

---

## 📄 License

Orca is licensed under the [Business Source License (BSL) 1.1](./LICENSE.md).

- Free for companies under £10 million total value (including production use).
- Free for trial and evaluation by companies over £10 million.
- Free for registered charities and educational institutions.
- No one may build competing software on top of Orca.

**Change Date:**
Each Orca version will automatically become open source under the GPLv3 license four (4) years after its first public release.

For full license terms, see [LICENSE.md](./LICENSE.md).
