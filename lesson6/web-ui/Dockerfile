FROM golang:1.21-alpine as builder
WORKDIR /app
COPY main.go .
RUN CGO_ENABLED=0 GOOS=linux go build -o server main.go

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/server .
COPY web ./web
EXPOSE 8080
CMD ["./server"]
