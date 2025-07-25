// server/config/logger.js
import chalk from 'chalk';

const levels = {
  info: chalk.blue,
  warn: chalk.yellow,
  error: chalk.red,
  success: chalk.green,
  debug: chalk.magenta,
};

const log = (level, message) => {
  const color = levels[level] || chalk.white;
  const timestamp = new Date().toISOString();
  console.log(`${chalk.gray(`[${timestamp}]`)} ${color(`[${level.toUpperCase()}]`)} ${message}`);
};

// Shortcut methods
export const logger = {
  info: (msg) => log('info', msg),
  warn: (msg) => log('warn', msg),
  error: (msg) => log('error', msg),
  success: (msg) => log('success', msg),
  debug: (msg) => {
    if (process.env.NODE_ENV !== 'production') {
      log('debug', msg);
    }
  },
};