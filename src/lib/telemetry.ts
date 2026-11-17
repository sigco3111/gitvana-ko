// Telemetry is disabled in the Korean fork: no visit or gameplay events are
// sent anywhere. The original project posted them to its own /api/events server.
export function initTelemetry(): void {}

export function trackEvent(_type: string, _levelId?: string | null, _data?: Record<string, unknown>): void {}
