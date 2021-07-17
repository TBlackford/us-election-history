// I want all exceptions to have the same messages

// Hopefully, the user never sees this issue - it is only for development
export const ImplementationException: Error = new Error('Not yet implemented');
