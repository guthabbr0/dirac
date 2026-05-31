export type ApiClientOptions = {
  baseUrl: string;
  token?: string;
};

export async function apiGet<T>(path: string, options: ApiClientOptions): Promise<T> {
  const response = await fetch(`${options.baseUrl}${path}`, {
    headers: options.token ? { Authorization: `Bearer ${options.token}` } : {},
  });
  if (!response.ok) {
    throw new Error(`Dirac API ${response.status}: ${await response.text()}`);
  }
  return (await response.json()) as T;
}
