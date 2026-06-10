FROM golang:1.26-alpine as builder
WORKDIR /app
COPY main.go .
RUN CGO_ENABLED=0 GOOS=linux go build -o server main.go

FROM alpine:latest
RUN apk update && apk upgrade --no-cache
WORKDIR /app
COPY --from=builder /app/server .
COPY web ./web
EXPOSE 8080
CMD ["./server"]
