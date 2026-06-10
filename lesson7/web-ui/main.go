package main

import (
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
	"os"
)

func main() {
	// Адрес бэкенда берем из переменной окружения, по умолчанию http://app:8000
	backendURL, _ := url.Parse(getEnv("API_URL", "http://app:8000"))
	proxy := httputil.NewSingleHostReverseProxy(backendURL)

	// Проксируем запросы /api/ на бэкенд (обрезая префикс /api)
	http.Handle("/api/", http.StripPrefix("/api", proxy))

	// Отдаем статику из папки ./web
	fs := http.FileServer(http.Dir("./web"))
	http.Handle("/", fs)

	log.Println("Frontend UI starting on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func getEnv(key, fallback string) string {
	if value, ok := os.LookupEnv(key); ok {
		return value
	}
	return fallback
}
